var express = require('express');
var router = express.Router();

const controllers = require('./../controllers');

/* REST API for picture order */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});

module.exports = router;
