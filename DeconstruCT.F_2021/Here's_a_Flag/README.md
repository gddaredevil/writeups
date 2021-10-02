# Here's a Flag

(Web, 150, 223 Solves)

A quick teaser to get yourself ready for the challenges to come! Just look for/at the flag and perhaps try your hand at some frontend tomfoolery?

`very.uniquename.xyz:2086`

### Investigation

Upon opening the above mentioned link, you'll be greeted with a pretty basic page with a flag image on it. 

The first point of analysis, as usual is to read the source code. It contains a sample flag meant for teasing.

Source code has two links: [styles.css](http://very.uniquename.xyz:2086/styles.css) and [index.js](http://very.uniquename.xyz:2086/index.js)

Information is index.js is provided only to mislead you and eat your time.

Check the styles.css webpage. The flag is embedded in it as `gvf{zh0frph_wr_ghfrqvwuxfwi}` and it is mentioned that it is a caesar cipher with a key of +3.

Decoding it will give the flag:

`dsc{we1come_to_deconstructf}`
