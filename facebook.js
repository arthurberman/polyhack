/*Facebook API functions used*/

/*Facebook setup to call right after <body>*/
function fbsetup(){
	window.fbAsyncInit = function() {
		FB.init({
			appID	: '656556201132796',
			xfbml	: true,
			version	: 'v2.1'
		});
	};
	(function(d, s, id){
		var js, fjs = d.getElementByTagName(s)[0];
		if (d.getElementById(id)) {return;}
		js = d.createElement(s); js.id = id;
		js.src = "//connect.facebook.net/e_US/sdk.js";
		fjs.parentNode.insertBefore(js, fjs);
	} (document, 'script', 'facebook-jssdk'));
}

/*Facebook share to call when sharing link to group*/
function fbshare(secretlink){
	FB.ui(
		{
			method: 'share',
			href: secretlink
		}, function(response){});

}

/*Facebook login to call with login button press*/
function fblogin(){
	FB.getLoginStatus(function(response){
		if(response.status === 'connected'){
			console.log('Logged in.');
		} else {
			FB.login();
		}
	});
}
