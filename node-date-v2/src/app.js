const express = require('express')
const moment = require('moment')

const app = express()

app.get('/date', (req, res) => {
    res.set('Content-Type', 'application/json');
    res.send(`{"date": "${moment().format('YYYY-MM-DD hh:mm:ss')}"}`)
})

app.listen(3001, () => console.log('Example app listening on port 3001!'))
