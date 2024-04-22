import winrm

# Initialize WinRM session
session = winrm.Session('localhost', auth=('username', 'password'))

def list_firewall_rules():
    # PowerShell command to list firewall rules
    ps_command = 'Get-NetFirewallRule | Select Name, DisplayName, Action, Direction, Enabled, Profile | ConvertTo-Json'

    # Execute PowerShell command
    result = session.run_ps(ps_command)

    # Print firewall rules
    print("[*] Firewall Rules:")
    for rule in result.std_out:
        print(rule)

def create_firewall_rule(name, display_name, action, direction, protocol, local_port, remote_address):
    # PowerShell command to create firewall rule
    ps_command = f'New-NetFirewallRule -Name "{name}" -DisplayName "{display_name}" -Action {action} -Direction {direction} -Protocol {protocol} -LocalPort {local_port} -RemoteAddress {remote_address}'

    # Execute PowerShell command
    session.run_ps(ps_command)
    print(f"[*] Created firewall rule: {name}")

def delete_firewall_rule(name):
    # PowerShell command to delete firewall rule
    ps_command = f'Remove-NetFirewallRule -Name "{name}"'

    # Execute PowerShell command
    session.run_ps(ps_command)
    print(f"[*] Deleted firewall rule: {name}")

if __name__ == "__main__":
    # List existing firewall rules
    list_firewall_rules()

    # Create a new firewall rule
    create_firewall_rule(
        name='MyCustomRule',
        display_name='My Custom Rule',
        action='Allow',
        direction='Inbound',
        protocol='TCP',
        local_port='8080',
        remote_address='Any'
    )

    # Delete the created firewall rule
    delete_firewall_rule(name='MyCustomRule')
