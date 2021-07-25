document.addEventListener('DOMContentLoaded', function() {


	
	var btn_sub = document.querySelector("#compose-form");
	

	
		
		
			document.querySelector("label").innerHTML ="";
		
		
			btn_sub.onsubmit = function(){
				console.log("Pressed");
				document.querySelector("label").innerHTML ="";
				let comment_content = document.querySelector("textarea").value;
				
				dummy_div = document.createElement("div");
				dummy_p = document.createElement("p");
				
				console.log(comment_content);
				fetch("/new_posts", {
						method : "post",
						body : JSON.stringify({
							author : "",
							content : comment_content
						})
					})
					.then(r => r.json())
					.then((p) => {console.log(p);
								dummy_p.innerText = p.content;
								dummy_p.id = "dummy"})
					.catch(error => console.log(error));
				
				
				dummy_div.append(dummy_p);
				document.querySelector(".body").append(dummy_div);
					
				
				
				return false;
			}
		
	

		
	
/*-------------------------------------------------------------*/

/*document.addEventListener('DOMContentLoaded', function(){
	console.log("Pressed")
	//document.querySelector(".navbar-nav mr-auto").style.display = 'none';
	//document.querySelector("#compose-posts").style.display = 'block';
	
	window.onscroll = () => {
	let start = 0;
	let number = 5;
	
	if (window.scrollY + window.innerHeight >= document.body.offsetHeight){
		document.querySelector("body").style.background = "red";
		get_some_posts(start, start + number);
		start = start + number;
	}
};
})*/
});
	


const get_all_posts = function(){
	
	fetch("/posts")
	.then(r => r.json())
	.then(posts => {
		posts.forEach( post => {
			console.log(post);
			let comment_div = document.createElement("div");
			comment_div.className = "post-div";
			comment_div.innerText = post.content;
			document.querySelector("#compose-posts").append(comment_div);
		});
	}).catch(error => {
		console.log(error);
	});
	
}



const get_some_posts = function(start, end){
	
	
	fetch("/posts?start=${start}&end=${end}#")
	.then(r => r.json())
	.then(posts => {
		posts.forEach( posts => {
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
	
	single_post.append(post_author);
	single_post.append(post_content);
	
	return single_post;
	
}