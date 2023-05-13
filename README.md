# Thelemic Date Class for Python

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![GitHub Issues](https://img.shields.io/github/issues/your-username/your-repo.svg)](https://github.com/your-username/your-repo/issues)
[![GitHub Stars](https://img.shields.io/github/stars/your-username/your-repo.svg)](https://github.com/your-username/your-repo/stargazers)

Do what thou wilt shall be the whole of the Law. 

Welcome to Thelemic Date Class for Python! This Python package allows you to work with Thelemic dates, providing methods to obtain the current Thelemic date or calculate a specific Thelemic date based on a given Gregorian date and time.

## Features

- Get the current Thelemic date for a specific location.
- Calculate a specific Thelemic date and time based on a given Gregorian date and time.
- Easy to use and integrate into your Python projects.

## Installation
Copy the ThelemicDateClass.py file into the same location you wish to call it from. 

## Usage
To use the Thelemic Date Class, follow the examples below:

```from ThelemicDateClass import ThelemicDate

## Get the current Thelemic date for a specific location
```date_data = ThelemicDate()
location = "Las Vegas, NV"
current_date = date_data.now(location)
print(current_date)

## Calculate a specific Thelemic date and time based on a given Gregorian date and time
```location = "Las Vegas, NV"
year, month, day, hour, minute = 1976, 1, 13, 8, 25
specific_day = date_data.in_day(year, month, day, hour, minute, location)
print(specific_day)```

## License
This project is licensed under the MIT License. For more information, please refer to the LICENSE file.

## Issues
If you encounter any issues or have suggestions for improvements, please feel free to open an issue. Your feedback is highly appreciated.

## Contributing
Contributions are welcome! If you would like to contribute to this project, please follow the guidelines in CONTRIBUTING.md.

## Acknowledgments
This project was inspired by the principles and practices of Thelema. I also want to personally thank all of thoe on my discord server, http://discord.gg/agapethelema 

## Contact
For any inquiries or questions, please contact the project maintainer, Lilith Vala Xara, lvx@dream.am

Love is the law, love under will.  

Lilith 
