import os
try:
    import distro
except ImportError:
    import platform

def clear_terminal():
    os.system('clear')

def custom_text(distro_name):
    print(f"""
            ┏━╸┏━┓┏━┓╺┳╸┏━╸┏━┓   ┏━┓┏━╸┏━┓┏━┓┏━┓╻╺┳╸┏━┓┏━┓╻ ╻
            ┣╸ ┣━┫┗━┓ ┃ ┣╸ ┣┳┛   ┣┳┛┣╸ ┣━┛┃ ┃┗━┓┃ ┃ ┃ ┃┣┳┛┗┳┛
            ╹  ╹ ╹┗━┛ ╹ ┗━╸╹┗╸   ╹┗╸┗━╸╹  ┗━┛┗━┛╹ ╹ ┗━┛╹┗╸ ╹ 
        ---------------------------------------------------------------
        |Creator: FerdinandDeroSaputra                                |
        |Inspired By: frozzipies                                      |
        |    This Will Make Updating and Upgrading Your Linux         |
        |                  repository 100% faster                     |
        ---------------------------------------------------------------
        You are currently using {distro_name}.
""")

def get_distro():
    try:
        dist_name = distro.name().lower()
        if 'ubuntu' in dist_name:
            return 'ubuntu'
        elif 'debian' in dist_name:
            return 'debian'
        elif 'kali' in dist_name:
            return 'kali'
        else:
            return 'unknown'
    except NameError:
        dist_name = platform.dist()[0].lower()
        if 'ubuntu' in dist_name:
            return 'ubuntu'
        elif 'debian' in dist_name:
            return 'debian'
        elif 'kali' in dist_name:
            return 'kali'
        else:
            return 'unknown'

def show_distro_info():
    distro_name = get_distro()
    print(f"Detected Linux Distribution: {distro_name.capitalize()}")

def handle_repo_for_distro(distro, action):
    repo_lines = {
        'ubuntu': [
            "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -cs) main restricted",
            "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -cs)-updates main restricted",
            "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -cs) universe",
            "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -cs)-updates universe",
            "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -cs) multiverse",
            "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -cs)-updates multiverse",
            "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -cs) backports",
            "deb http://security.ubuntu.com/ubuntu $(lsb_release -cs)-security main restricted",
            "deb http://security.ubuntu.com/ubuntu $(lsb_release -cs)-security universe",
            "deb http://security.ubuntu.com/ubuntu $(lsb_release -cs)-security multiverse"
        ],
        'debian': [
            "deb http://deb.debian.org/debian/ $(lsb_release -cs) main",
            "deb http://deb.debian.org/debian/ $(lsb_release -cs)-updates main",
            "deb http://security.debian.org/ $(lsb_release -cs)-security main"
        ],
        'kali': [
            "deb https://mirrors.ocf.berkeley.edu/kali/ kali-rolling main contrib non-free",
            "# For source package access, uncomment the following line",
            "# deb-src https://mirrors.ocf.berkeley.edu/kali/ kali-rolling main contrib non-free"
        ]
    }

    if not os.path.isfile('/etc/apt/sources.list.bak'):
        os.system('cp /etc/apt/sources.list /etc/apt/sources.list.bak')
        print("Original sources.list file has been backed up as sources.list.bak.")
    else:
        print("Backup of the original sources.list file (sources.list.bak) already exists.")

    temp_file = os.popen('mktemp').read().strip()

    if distro in repo_lines:
        if action == 'speed_up':
            with open('/etc/apt/sources.list', 'r') as f:
                for line in f:
                    os.system(f'echo "# {line.strip()}" >> {temp_file}')
            for new_line in repo_lines[distro]:
                os.system(f'echo "{new_line}" >> {temp_file}')
            os.system(f'mv {temp_file} /etc/apt/sources.list')
            os.system('sudo apt clean')
        elif action == 'add':
            for line in repo_lines[distro]:
                os.system(f'echo "{line}" >> /etc/apt/sources.list')
        os.system(f'rm -f {temp_file}')
    else:
        print("Unsupported distribution or unknown distribution.")

def update_and_upgrade_repository():
    os.system('sudo apt update -o Acquire::http::Pipeline-Depth=0 && sudo apt upgrade -y --fix-missing')
    clear_terminal()
    custom_text(get_distro())
    print("Repository has been updated and upgraded.")

def revert_to_old_repository():
    if os.path.isfile('/etc/apt/sources.list.bak'):
        os.system('cp /etc/apt/sources.list.bak /etc/apt/sources.list')
        clear_terminal()
        custom_text(get_distro())
        print("Repository has been reverted to the old configuration from sources.list.bak.")
    else:
        clear_terminal()
        custom_text(get_distro())
        print("No backup of the original sources.list file found. Cannot revert.")

def get_user_choice():
    distro_name = get_distro()
    show_distro_info()
    
    while True:
        print("\nChoose an option:")
        print("1. Speed up repository update & upgrade")
        print("2. Add repository (for non-default repos)")
        print("3. Update & Upgrade Repository")
        print("4. Revert to Old Repository")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            handle_repo_for_distro(distro_name, 'speed_up')
        elif choice == '2':
            handle_repo_for_distro(distro_name, 'add')
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
custom_text(get_distro())

while True:
    get_user_choice()
