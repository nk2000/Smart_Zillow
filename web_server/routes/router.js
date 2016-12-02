var express = require('express');
var passwordHash = require('password-hash');
var session = require('client-sessions');
var User = require('../model/user');


var router = express.Router();

TITLE = 'Smart Zillow';

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Smart Zillow' });
});

/* Login page */
router.get('/login', function(req, res, next) {
  res.render('login', { title: TITLE });
});

/* Register page */
router.get('/register', function(req, res, next) {
  res.render('register', { title: TITLE });
});


router.post('/register',function(req,res,next){
  //Get form values.
  var email = req.body.email;
  var password = req.body.password;
  var hashedPassword = passwordHash.generate(password);

  //Check if the email is already used. No blocking IO
  User.find({email:email},function(err,users){
    if(err) throw err;
    if(users.length >0){
      console.log("User found for:" + email);
      res.render('register',{
        title:TITLE,
        message:'Email is already used.Please pick a new one. Or<a href="/login">Login</a>'
      })
    }else{
      var newUser = User({
          email:email,
          password:hashedPassword,
      });
      //Save the user.
      newUser.save(function(err){
        if(err) throw err;
        console.log('User created!');
        req.session.user = email;
        res.redirect('/');
      });
    }
  });
});

module.exports = router;
