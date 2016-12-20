var jayson = require('jayson');

var client = jayson.client.http({
  hostname: 'localhost',
  port: 4040
});

//test RPC method add()

//this func helps us call backend func
function add(a, b, callback){
  client.request('add', [a, b], function(err, error, response){
      if (err) throw err;
      console.log(response);
      callback(response);
  });
}
//

function searchArea(query, callback){
  client.request('searchArea', [query], function(err, error, response){
      if (err) throw err;
      console.log(response);
      callback(response);
  });
}


//explore
module.exports = {
  add: add,
  searchArea: searchArea
}
