# TSC: Public Folder Index

## Overview

TSC: Public Folder Index is a custom-built graphical user interface (GUI) application designed to revolutionize the process of querying public folders and contacts within the Exchange server of our organization. This tool transforms a traditionally time-consuming task into an instantaneous operation, significantly enhancing productivity and efficiency.

## Key Features

- **Lightning-Fast Queries**: Search through over 7,800 paths in public folders and approximately 65,000 contact entries in less than 1 second.
- **User-Friendly Interface**: Built using the customtkinter library, ensuring ease of use for all skill levels.
- **Massive Time Savings**: Reduces query time from 6-8 minutes to less than 1-2 seconds per query.
- **Automated Index Updates**: Keeps the directory structure current with scheduled weekly or bi-monthly updates.

## Technical Highlights

- **Efficient Search Algorithm**: Utilizes a pre-built index for rapid search capabilities.
- **Standalone Executable**: Packaged with PyInstaller for easy deployment without additional software requirements.
- **Professional Installation**: Includes an installer created with Inno Setup for smooth deployment in enterprise environments.

## Requirements

- Windows 10 or later
- Microsoft Exchange Server environment
- Outlook with VBA capabilities (for automated index updates)

## Installation

1. Download the installer from the releases section.
2. Run the installer and follow the on-screen instructions.
3. For automated index updates, ensure the provided VBA scripts are added to Outlook and scheduled tasks are set up as per the installation guide.

## Usage

1. Launch the TSC: Public Folder Index application.
2. Enter your search query in the provided field.
3. Press enter or click the search button.
4. View the instantaneous results displayed in the application window.

## Automated Index Updates

To keep the index current:

1. Add the two provided VBA scripts to Outlook.
2. Set up two recurring appointments in Outlook to run these scripts.
3. Configure a scheduled task to update the index weekly or bi-monthly as preferred.

Detailed instructions for setting up automated updates can be found in the installation guide.

## Benefits

- **Significant Time Savings**: Reduce query times from hours to seconds.
- **Improved User Experience**: Simple interface encourages adoption and consistent usage.
- **Resource Optimization**: Automated updates minimize manual intervention and potential for human error.
- **Enhanced IT Support**: Enables quicker response times and better service to end-users.

## Technical Stack

- Python
- customtkinter (for GUI)
- PyInstaller (for executable packaging)
- Inno Setup (for installer creation)
- VBA (for automated index updates in Outlook)

## Contributing

While this is an internal tool, we welcome feedback and suggestions from our team members. Please submit any issues or enhancement ideas through our internal ticketing system.

## License

This software is proprietary and for internal use only. Unauthorized distribution or use outside of our organization is strictly prohibited.

## Acknowledgments

Special thanks to the UAMS IT Help Desk team for their support and feedback during the development of this tool.

---

Developed by Lee Charles for UAMS IT Help Desk
