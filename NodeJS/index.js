/**
 * Created by m1911 on 17/3/22.
 */
var origin = 'http://pilicreateworld.tw-blog.com/PILI/PILI';
var cheerio = require('cheerio');
var array = [];
var fs = require('fs');
var async = require('async');
var superagent = require('superagent');
var request = require('request');
var http = require('http');
var https = require('https');
var path = require('path');

request(origin + '67' + '/', function (error, response, body) {
  console.log(error, response, body);

  var $ = cheerio.load(body);
  $('ul li a').each(function (a, item) {
    var data = item.children[0].data;
    var folderName = data.trim();
    if (folderName.indexOf('HTM') !== -1) {
      request(origin + '67' + '/' + data.trim(), function (error, response, body) {
        var $ = cheerio.load(body);
        $('img').each(function (index, img) {
          var srcEle = img.attribs.src;
          if (srcEle.indexOf('http') === 0) {
            list.push(srcEle);
            downloadImg('~/m1911/WebstormProjects/', srcEle);
          }
        });
      });
    }
  });
});


function downloadImg(imgDir, url) {
  var proto = http;
  if (url.indexOf('https') === 0) {
    proto = https
  }
  proto.get(url, function(res) {
    var data = '';

    res.setEncoding('binary');

    res.on('data', function(chunk) {
      data += chunk;
    });

    res.on('end', function() {
      // 调用 fs.writeFile 方法保存图片到本地
      // path.basename(url) 可以得到链接指向的文件名
      // 如：path.basename('http://localhost/img/2.jpg') => '2.jpg'
      fs.writeFile('./' + path.basename(url), data, 'binary', function(err) {
        if (err) {
          return console.log(err);
        }
        console.log('Image downloaded:', path.basename(url));
      });
    });
  }).on('error', function(err) {
    console.log(err);
  });
}
