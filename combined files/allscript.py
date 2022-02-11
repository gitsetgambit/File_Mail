'''running all the scripts 
1st - combine.py
2nd - filemail.py
3rd - sendmails.py
4th - delete_used.py'''

import subprocess


def execute_script(script_path):

    print(f"starting execution of {script_path}")
    try:
        subprocess.run(["python", script_path], check=True)
    except Exception as exc:
        print(f"error during execution of {script_path}: {str(exc)}")
    else:
        print(f"finished execution of {script_path}")


execute_script("C:\\Users\\hp\\Desktop\\combined files\\combinefile.py")
execute_script("C:\\Users\\hp\\Desktop\\file_mail\\FileMail.py")
execute_script("C:\\Users\\hp\\Desktop\\file_mail\\sendMails.py")
execute_script("C:\\Users\\hp\\Desktop\\file_mail\\delete_used.py")
