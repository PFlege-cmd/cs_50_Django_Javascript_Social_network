document.addEventListener('DOMContentLoaded', function() {
	
	let start = 0;
	let difference = 5;
	
	get_some_posts(start, start+difference);
	
	start = start + difference;
	
	window.onscroll = () => {
			if (window.scrollY + window.innerHeight >= document.body.offsetHeight){
			//document.querySelector("body").style.background = "red";
			get_some_posts(start, start+difference)
			start = start + difference ;
		} 
	}

	

});

const get_some_posts = function(start, end){
	
	
	fetch(`/posts?start=${start}&end=${end}#`)
	.then(r => r.json())
	.then(posts => {
		posts.forEach( post => {
			document.querySelector("#compose-posts").append(create_a_post_div(post));
		})
		}).catch(error => {
		console.log(error);
	});
	
}

const create_a_post_div = function(json){
	single_post = document.createElement("div");
	
	post_author = document.createElement("div");
	post_content = document.createElement("div");
	
	post_author.innerText = json.author;
	post_content.innerText = json.content;
	
	post_author.style.border = "thin dotted black";
	
	single_post.append(post_author);
	single_post.append(post_content);
	
	single_post.style.border = "thick solid black";
	single_post.style.height = "100px";
	
	return single_post;
	
}