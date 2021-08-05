document.addEventListener('DOMContentLoaded', function() {
	
	console.log(JSON.parse(document.querySelector("#user_name").textContent));
	
	const current_user = JSON.parse(document.querySelector("#user_name").textContent)
	// The above is actually completely unnecessary, as I can get the username from the above list.
	// Nevertheless, for training purposes, I leave it here!
	
	// Continue here tomorrow! Above is the solution!
	let start = 0;
	let difference = 5;
	
	get_some_posts(start, start+difference, current_user);
	
	start = start + difference;
	
	window.onscroll = () => {
			if (window.scrollY + window.innerHeight >= document.body.offsetHeight){
			get_some_posts(start, start+difference, current_user)
			start = start + difference ;
		} 
	}

	

});

const get_some_posts = function(start, end, current_user){
	
	
	fetch(`/posts?start=${start}&end=${end}#`)
	.then(r => r.json())
	.then(posts => {
		posts.forEach( post => {
			document.querySelector("#compose-posts").append(create_a_post_div(post, current_user));
		})
		}).catch(error => {
		console.log(error);
	});
	
}

const create_a_post_div = function(json, current_user){
	let single_post = document.createElement("div");
	
	
	let post_content = document.createElement("div");
	post_content.innerText = json.content;
	post_content.className = "post_content";
		
	let link_to_user = document.createElement("a");
	link_to_user.innerText = json.author;
	
	let StringJson = json.author.toString();
	link_to_user.href = '/profile/' + json.author.toString();
	
	let post_author = document.createElement("div");
	post_author.style.border = "thin dotted black";
	post_author.className = "post_author";
	post_author.append(link_to_user);
	
	if (current_user === json.author){
	
		let edit_button = document.createElement("button");
		edit_button.className = "edit";
		edit_button.textContent = "Save";
		post_content.append(edit_button);
		
		edit_button.onclick = function(){
			edit_button.disabled = true;
			//single_post.style.height = "450px";
			//post_content.style.height = "100%";
			
			edit_form = document.createElement("form");
			text_input = document.createElement("textarea");
			text_input.value = json.content;
			text_input.className = "text_input";
			text_input.TextMode="MultiLine"
			//text_input.style.height = "300px";
			
			edit_form.style.height = "100%"
			text_input.cols = "10"
			//text_input.style.width = "50%";
			//text_input.style.height = "50%";
			
			text_input.style.textAlign = "left";
			single_post.style.height = "450px"
			
			text_submit = document.createElement("button");
			text_submit.textContent = "Commit";
	
			edit_form.appendChild(text_input);
			edit_form.appendChild(text_submit);
	
			console.log(edit_form);
			post_content.appendChild(edit_form);
			
			text_submit.onclick = function(){
				fetch('/posts', {
					method: "put",
					body: JSON.stringify({
						post_id : json.id,
						post_content: text_input.value
					})
				}).then(post => console.log(post))
				.catch(error => console.log(error))			
			}
			
		}
		
		
	}
	
	post_author.style.border = "thin dotted black";
	post_author.append(link_to_user);
	
	single_post.append(post_author);
	single_post.append(post_content);
	
	single_post.style.border = "thick solid black";
	single_post.style.height = "100px";
	
	
	single_post.id = json.id;
	single_post.className = "posts";
	single_post.classList.add(json.author);
	
	return single_post;
	
}

const edit_data = function(id, post_content){
	edit_form = document.createElement("form");
	text_input = document.createElement("input");
	text_submit = document.createElement("input");
	
	text_input.type = "textarea";
	text_submit.type = "submit";
	
	edit_form.appendChild(text_input);
	edit_form.appendChild(text_submit);
	
	console.log(edit_form);
	//post_content.appendChild(edit_form);
	
	
}