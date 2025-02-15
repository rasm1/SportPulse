
const deleteModalpost = new bootstrap.Modal(document.getElementById("deleteModalpost"));
const deleteButtonsPost = document.getElementsByClassName("btn-delete-post");
const deleteConfirmPost = document.getElementById("deleteConfirmPost");



/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtonsPost) {
  button.addEventListener("click", (e) => {
    let postId = e.target.getAttribute("post_id");
    deleteConfirmPost.href = `delete_post/${postId}`;
    deleteModalpost.show();
  });
}


