var client = require('./rpc_client');

client.add(1, 2, function(response){
  console.log('1 + 2 =' + response);
});
