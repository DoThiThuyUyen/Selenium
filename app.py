from imap_tools import MailBox

def read_emails(username: str, password: str, folder: str = 'Inbox', limit: int = 1):
    with MailBox("imap.gmail.com").login(username, password, folder) as mb:
    
        for msg in mb.fetch(limit=limit, reverse=True, mark_seen=False):
            print(f"CODE: {msg.uid}\n")

# Ví dụ sử dụng hàm
read_emails('dothithuyuyen0601@gmail.com', 'ohuwrsygzwhenhfe')
