from twisted.internet import reactor, protocol
from twisted.conch import avatar, recvline
from twisted.conch.ssh import factory, keys, userauth, connection, session

class FakeAvatar(avatar.ConchUser):
    def __init__(self, username):
        avatar.ConchUser.__init__(self)
        self.username = username
        self.channelLookup.update({"session": session.SSHSession})

    def openShell(self, protocol):
        serverProtocol = protocol.ServerProtocol()
        serverProtocol.makeConnection(recvline.HistoricRecvLine())
        protocol.makeConnection(session.wrapProtocol(serverProtocol))

class FakeFactory(factory.SSHFactory):
    publicKeys = {
        'ssh-rsa': keys.Key.fromString(data=b"""AAAAB3NzaC1yc2EAAAADAQABAAABAQDNc9xZLxXpK07ZTgll77rF3knhDf69vDBYjQkA
        gXzGwCV6cCXYJQTF/s5te1q6Oz0QJwe1CQWzkyqSmt00f4lDMH7rl72bFzO1xgBQm/H4U49EXRw
        uHrKZj/BzNBBYU1rO8jQKhiCUn5vJyYmU5cGTQc8dQdVYkUj2hGp7jzSM84Rn0rDtkv/qv9QJrNa
        Z54eY5iD7wBI4trF5rOT/Ux76TnxYwsdGF5UuxF4m/wzd0KbT8c7G2EgXH29rYt7byjBxFkl5MN
        GwQwWNE7QKrLeZ4IzgR9YiGolYdEnmQrEys0bqMmz0Uc5hqHu6zPiiOyYWDx7dDv/0gTK5vObAD
        """),
    }
    privateKeys = {
        'ssh-rsa': keys.Key.fromString(data=b"""AAAAB3NzaC1yc2EAAAADAQABAAABAQDNc9xZLxXpK07ZTgll77rF3knhDf69vDBYjQkA
        gXzGwCV6cCXYJQTF/s5te1q6Oz0QJwe1CQWzkyqSmt00f4lDMH7rl72bFzO1xgBQm/H4U49EXRw
        uHrKZj/BzNBBYU1rO8jQKhiCUn5vJyYmU5cGTQc8dQdVYkUj2hGp7jzSM84Rn0rDtkv/qv9QJrNa
        Z54eY5iD7wBI4trF5rOT/Ux76TnxYwsdGF5UuxF4m/wzd0KbT8c7G2EgXH29rYt7byjBxFkl5MN
        GwQwWNE7QKrLeZ4IzgR9YiGolYdEnmQrEys0bqMmz0Uc5hqHu6zPiiOyYWDx7dDv/0gTK5vObAD
        """),
    }
    
    def __init__(self):
        factory.SSHFactory.__init__(self)
        self.portal = None

    def buildProtocol(self, addr):
        return connection.SSHConnection()

    def startFactory(self):
        self.portal = portal.Portal(FakeRealm())
        self.portal.registerChecker(userauth.UserAuthenticator())
        self.portal.registerChecker(userauth.ConchUserDirectory())

class FakeRealm:
    def requestAvatar(self, avatarId, mind, *interfaces):
        if avatar.ConchUser in interfaces:
            return avatar.ConchUser, FakeAvatar(avatarId), lambda: None
        raise Exception("No supported interfaces found.")

if __name__ == "__main__":
    reactor.listenTCP(2222, FakeFactory())
    print("[*] SSH honeypot started on port 2222")
    reactor.run()
