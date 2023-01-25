// Run this script on your discord server to get your server's stickers.
// Namely, to use it you have to turn on your inspection tools of your browser
// On Chrome based browsers, on the menu bar, click on  View -> Developer -> Developer Tools

// Then, click on the emoji button on the bottom right of the message input box
// Then, a small subwindow of emojis will appear

// Try to have your inspector focus on one of the emojis.

// On your console of your inspector tools, run the following code:
// You should get your results in a nice json list.
// Save the nice json output into a file for the python script to use.
// I like to save the stickers in a file called stickers.json

result = []
document.querySelectorAll('#emoji-picker-grid > div > div > div > div > ul > li > button > img')
    .forEach(node => result.push([node.getAttribute('alt'), node.getAttribute('src')]))
console.log(result)