const express = require('express')
const app = express()

let counter = 0

app.get('/counter', (req, res) => {
    res.set('Content-Type', 'application/json');
    res.send(`{"counter": ${counter}}`)
    counter=counter+1
})

app.listen(3000, () => console.log('Example app listening on port 3000!'))
