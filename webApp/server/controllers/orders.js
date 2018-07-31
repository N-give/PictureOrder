const arangojs = require('arangojs');
const aql = require('arangojs').aql;
const db = new arangojs.Database();
db.useDatabase('photoTest');
/*
 * Add database authentication here
 */

const orCollection = db.collection('orders');

async function find(req, res){
  return db.query(aql`
    FOR ord IN ${orCollection}
      SORT ord.test
      RETURN ord
  `);
}

async function create(req, res){
  return db.query(aql`
    FOR order IN ${req.body.orders}
      INSERT order INTO ${orCollection}
      RETURN order
  `);
}

async function update(req, res){
  return db.query(aql`
    FOR order IN ${req.body.orders}
      FOR ord IN ${orCollection}
        FILTER order._key == ord._key
        UPDATE ord._key
        WITH order INTO ${orCollection}
        RETURN NEW 
  `);
}

async function remove(req, res){
  return db.query(aql`
    FOR order IN ${req.body.orders}
      FOR ord IN ${orCollection}
        FILTER order._key == ord._key
        REMOVE ord._key
        INTO ${orCollection}
        RETURN OLD
  `);
}

module.exports = {
  find,
  create,
  update,
  remove
};
