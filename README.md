# Remify plugin for Sublime Text 3

Converts 

`margin: 4px` 

to

`+rem(margin, 4px)`

Very specific use case, assuming you are using `.sass` files and a mixin called `rem` to convert pixels to ems.

## Installation

### [Sublime Package Control](http://wbond.net/sublime_packages/package_control)

In the command Pallette choose **Package Control: Install Package** and select **Remify**

### Git installation

Clone the repository in your Sublime Text "Packages" directory:

    git clone https://github.com/brousalis/remify.git "Remify"

The "Packages" directory is located at:

* OS X:

        ~/Library/Application Support/Sublime Text 3/Packages/

* Linux:

        ~/.config/sublime-text-3/Packages/

* Windows:

        %APPDATA%/Sublime Text 3/Packages/

## Usage

* **Convert line** `shift + super + s` - replaces pixels with +rem(prop, value)  

### In Command Palette:

* **Remify: Convert line**
