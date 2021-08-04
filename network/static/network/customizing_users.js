document.addEventListener('DOMContentLoaded', function() {
	
	
	var displayed_user_name = document.querySelector("h1").textContent.toString();
	
	let start = 0;
	let difference = 5;
	
	get_some_posts(start, start+difference, displayed_user_name);
	
	start = start + difference;
	
	window.onscroll = () => {
			if (window.scrollY + window.innerHeight >= document.body.offsetHeight){
			get_some_posts(start, start+difference, displayed_user_name)
			start = start + difference ;
		} 
	}

	document.querySelector("#follow-btn").onclick  = function(){
		fetch('/profile/' + displayed_user_name, {
			method : "put",
			body: JSON.stringify({
				follow: displayed_user_name,
				unfollow: false
			})
		})
		.then(user =>{
		console.log(user.status);}
		)
		.catch(error => console.log(error));
			
	}
	
	document.querySelector("#unfollow-btn").onclick  = function(){
		fetch('/profile/' + displayed_user_name, {
			method : "put",
			body: JSON.stringify({
				follow: displayed_user_name,
				unfollow: true
			})
		})
		.then(user =>{
		console.log(user.status);}
		)
		.catch(error => console.log(error));
			
	}
	
	
		
});


const get_some_posts = function(start, end, displayed_user_name){
	
	
	fetch("/profile/" + displayed_user_name + "/posts?start=" + start + "&end=" + end)
	.then(r => r.json())
	.then(posts => {
		posts.forEach( post => {
			document.querySelector("#user-info").append(create_a_post_div(post));
			console.log(post);
		})
		}).catch(error => {
		console.log(error);
	});
	
}

const create_a_post_div = function(json){
	single_post = document.createElement("div");
	
	post_content = document.createElement("div");
	post_content.innerText = json.content;
		
	link_to_user = document.createElement("a");
	link_to_user.innerText = json.author;
	
	StringJson = json.author.toString();
	link_to_user.href = '/profile/' + json.author.toString();
	
	post_author = document.createElement("div");
	post_author.style.border = "thin dotted black";
	post_author.append(link_to_user);
	
	
	post_author.style.border = "thin dotted black";
	post_author.append(link_to_user);
	
	single_post.append(post_author);
	single_post.append(post_content);
	
	single_post.style.border = "thick solid black";
	single_post.style.height = "100px";
	
	
	single_post.id = json.id;
	single_post.className = "posts";
	
	return single_post;
	
}