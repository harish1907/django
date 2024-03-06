function confirmDelete(id, deleteUrl) {
  if (confirm("Are you sure you want to delete this item?")) {
    const form = document.createElement("form");
    form.method = "post";
    form.action = deleteUrl;

    const csrfToken = document.querySelector(
      "[name=csrfmiddlewaretoken]"
    ).value;
    const csrfInput = document.createElement("input");
    csrfInput.type = "hidden";
    csrfInput.name = "csrfmiddlewaretoken";
    csrfInput.value = csrfToken;

    form.appendChild(csrfInput);

    document.body.appendChild(form);
    form.submit();
  }
}
