document.addEventListener('DOMContentLoaded', function() {
	
	
	var displayed_user_name = document.querySelector("h1").textContent.toString();
	
	let start = 0;
	let difference = 5;
	
	get_some_posts(start, start+6, displayed_user_name);
	
	start = start + difference;
	
	window.onscroll = () => {
			if (window.scrollY + window.innerHeight >= document.body.offsetHeight){
			get_some_posts(start, start+difference, displayed_user_name)
			start = start + difference ;
		} 
	}
	
			
});

const get_some_posts = function(start, end){
	
	
	fetch(`/posts?start=${start}&end=${end}&followers=True#`)
	.then(r => r.json())
	.then(posts => {
		posts.forEach( post => {
			document.querySelector("#following-info").append(create_a_post_div(post));
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