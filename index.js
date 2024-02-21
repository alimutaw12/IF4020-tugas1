const express = require('express');
const app = express();
const port = 3000;

app.set('view engine', 'pug');
app.get('/', function (req, res) {
    res.render("index", { title: "Hey", message: "Hello there!" });
});

app.get("/encrypt/:cipher/:text/:key", function (req, res) {
    const { cipher, text, key } = req.params;
  
    switch (cipher) {
        case "vigenere":
            res.send({
                data: intListToText(
                    encryptVigenere(textToIntList(text), textToIntList(key))
                ),
            });
            break;
  
        default:
            break;
    }
});

app.get("/decrypt/:algoritme/:text/:key", function (req, res) {
    const { algoritme, text, key } = req.params;
  
    switch (algoritme) {
        case "vigenere":
            res.send({
                data: intListToText(
                    decryptVigenere(textToIntList(text), textToIntList(key))
                ),
            });
            break;
  
        default:
            break;
    }
});

app.listen(port, () => console.log('Test running'));