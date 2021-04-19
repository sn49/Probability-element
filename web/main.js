var level=0
var http = require('http');
var fs = require('fs');
var app = http.createServer(function(request,response){
var url = request.url;
response.writeHead(200);
if(request.url == '/'){
    url = '/index.html';
    level++
    response.write(level.toString())
}
else if(request.url == '/register'){
    url='/register.html'
}   
if(request.url == '/favicon.ico'){
response.writeHead(404);

response.end();
return;
}


response.end(fs.readFileSync(__dirname + url));


});
app.listen(3000);