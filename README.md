## Assembly

Setup Windows Machine In A Automated Manner

## Purpose?

When you have a fresh `Operating System` you may find yourself spending a long time installing applications and setting up the registry how you want it. I'm sure you dont have time for that and would appreciate if something did it all for you. Well Assembly is a one time setup script written in `Python`. You can easily configure and possibly put it on your <a target="_blank" href="https://www.raspberrypi.com/products/raspberry-pi-pico/">`Raspberry Pi Pico`</a> or another `HID` device so it automatically runs and does the hard work for you.


## Usage

Your json file is very crucial to get this software to work and to keep the storage capcity needed limited.

Here you will need to fill out the fields so the `HID` can download and remove the files after usage.

`setup_type` is the type of setup you want. (Full or Custom)
`gamer` Setting this to True will install Game libraries such as `Steam` onto your PC.
`Custom_Cursors` This will install your custom cursors and apply them in the registry.

```json

{
    "setup_type": "full",
    "gamer": "True_or_False",
    "Custom_Cursors": "Cursors_File_URL_Here"
}

```

