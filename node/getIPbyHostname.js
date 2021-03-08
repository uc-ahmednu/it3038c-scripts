var path = require("path"); 
var dns = require(`dns`);

function hostnameLookup(h) {
    dns.lookup(hostname,function(err,addresses,family){
        console.log(addresses);
    });
}
if (process.argv.length <= 2) {
    console.log(`USAGE: node ${path.basename(__filename)} hostname.com`)
    process.exit(-1)
}

var hostname = process.argv[2]
console.log(`Checking IP of: ${hostname}`)
hostnameLookup(hostname);