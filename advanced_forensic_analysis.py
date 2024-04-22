import Evtx.Evtx as evtx
import Evtx.Views as e_views

def parse_evtx_file(file_path):
    try:
        with evtx.Evtx(file_path) as log:
            records = [record for record in log.records()]
            
            print(f"[*] Parsing Windows Event Log file: {file_path}")
            print(f"[*] Total records found: {len(records)}\n")
            
            for record in records:
                event = e_views.EVTX(record)
                
                print(f"Record ID: {event.record_id()}")
                print(f"Event Level: {event.level()}")
                print(f"Event Time: {event.timestamp()}")
                print(f"Event Provider: {event.provider()}")
                print(f"Event Description: {event.description()}\n")

    except Exception as e:
        print(f"Error parsing the Evtx file: {e}")

if __name__ == "__main__":
    file_path = input("Enter the path to the Windows Event Log (.evtx) file to analyze: ")
    parse_evtx_file(file_path)
