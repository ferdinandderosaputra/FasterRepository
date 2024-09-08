import os

def clear_terminal():
    os.system('clear')


def custom_text():
    print("""
        ┏━╸┏━┓┏━┓╺┳╸┏━╸┏━┓   ╻┏ ┏━┓╻  ╻   ┏━┓┏━╸┏━┓┏━┓┏━┓╻╺┳╸┏━┓┏━┓╻ ╻
        ┣╸ ┣━┫┗━┓ ┃ ┣╸ ┣┳┛   ┣┻┓┣━┫┃  ┃   ┣┳┛┣╸ ┣━┛┃ ┃┗━┓┃ ┃ ┃ ┃┣┳┛┗┳┛
        ╹  ╹ ╹┗━┛ ╹ ┗━╸╹┗╸   ╹ ╹╹ ╹┗━╸╹   ╹┗╸┗━╸╹  ┗━┛┗━┛╹ ╹ ┗━┛╹┗╸ ╹ 
        --------------------------------------------------------------
        |Creator:FerzChills                                          |
        |Inspired By:frozzipies                                      |
        |    This Will Make Updating and Upgrading Your Kali Linux   |
        |                  repository 100% faster                    |
        --------------------------------------------------------------
""")

def speed_up_repository():
    if not os.path.isfile('/etc/apt/sources.list.bak'):
        os.system('cp /etc/apt/sources.list /etc/apt/sources.list.bak')
        print("Original sources.list file has been backed up as sources.list.bak.")
    else:
        print("Backup of the original sources.list file (sources.list.bak) already exists.")

    new_lines = [
        "deb https://mirrors.ocf.berkeley.edu/kali/ kali-rolling main contrib non-free",
        "# For source package access, uncomment the following line",
        "# deb-src https://mirrors.ocf.berkeley.edu/kali/ kali-rolling main contrib non-free"
    ]

    temp_file = os.popen('mktemp').read().strip()

    with open('/etc/apt/sources.list', 'r') as f:
        for line in f:
            os.system(f'echo "# {line.strip()}" >> {temp_file}')

    for new_line in new_lines:
        os.system(f'echo "{new_line}" >> {temp_file}')

    os.system(f'mv {temp_file} /etc/apt/sources.list')

    os.system(f'rm -f {temp_file}')

    os.system('sudo apt clean')

    clear_terminal()

    custom_text()

    print("Repository configuration updated, and package cache cleaned.")

def update_and_upgrade_repository():
    os.system('sudo apt update && sudo apt upgrade -y')

    clear_terminal()

    custom_text()

    print("Repository has been updated and upgraded.")

def revert_to_old_repository():
    if os.path.isfile('/etc/apt/sources.list.bak'):
        os.system('cp /etc/apt/sources.list.bak /etc/apt/sources.list')

        clear_terminal()

        custom_text()

        print("Repository has been reverted to the old configuration from sources.list.bak.")
    else:
        clear_terminal()

        custom_text()

        print("No backup of the original sources.list file found. Cannot revert.")

def add_kali_repository():
    if not os.path.isfile('/etc/apt/sources.list.bak'):
        os.system('cp /etc/apt/sources.list /etc/apt/sources.list.bak')
        print("Original sources.list file has been backed up as sources.list.bak.")
    else:
        print("Backup of the original sources.list file (sources.list.bak) already exists.")

    kali_lines = [
        "deb https://mirrors.ocf.berkeley.edu/kali/ kali-rolling main contrib non-free",
        "# For source package access, uncomment the following line",
        "# deb-src https://mirrors.ocf.berkeley.edu/kali/ kali-rolling main contrib non-free"
    ]

    for kali_line in kali_lines:
        os.system(f'echo "{kali_line}" >> /etc/apt/sources.list')

    clear_terminal()

    custom_text()

    print("Kali repository has been added to the sources.list file.")

def get_user_choice():
    while True:
        print("Choose an option:")
        print("1. Speed up your Kali Repository Update && Upgrade")
        print("2. Add Kali Repository (for non-Kali distro)")
        print("3. Update & Upgrade Repository")
        print("4. Back to Old Repository")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            speed_up_repository()
        elif choice == '2':
            add_kali_repository()
        elif choice == '3':
            update_and_upgrade_repository()
        elif choice == '4':
            revert_to_old_repository()
        elif choice == '5':
            print("Exiting.")
            os.system("sleep 2")
            os.system("clear")
            exit(0)
        else:
            print("Invalid choice. Please try again.")

clear_terminal()
custom_text()

while True:
    get_user_choice()