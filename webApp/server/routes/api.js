const express = require('express');
const router = express.Router();
const controllers = require('./../controllers');

router.get('/', function(req, res) {
  res.send("Respond with a resource");
});

router.get('/:resource', async function(req, res){
  // console.log(req.params);
  const controller = controllers[req.params.resource];
  const docs = await controller.find(req, res);
  console.log(docs);
  res.json({confimation: 'success', result: docs._result});
});

router.post('/:resource', async function(req, res){
  const controller = controllers[req.params.resource];
  const docs = await controller.create(req, res);
  res.json({confirmation: 'success', result: docs._result});
});

router.put('/:resource', async function(req, res){
  const controller = controllers[req.params.resource];
  const docs = await controller.update(req, res);
  res.json({confirmation: 'success', result: docs._result});
});

router.delete('/:resource', async function(req, res){
  const controller = controllers[req.params.resource];
  const docs = await controller.remove(req, res);
  res.json({confirmation: 'success', result: docs._result});
});

module.exports = router;
