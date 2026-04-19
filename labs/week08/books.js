// Show the create form
function showCreate() {
    document.getElementById('button-showCreate').style.display = "none";
    document.getElementById('bookTable').style.display = "none";
    document.getElementById('createUpdateForm').style.display = "block";

    // show create mode
    document.getElementById('createLabel').style.display = "inline";
    document.getElementById('updateLabel').style.display = "none";
    document.getElementById('button-doCreate').style.display = "inline";
    document.getElementById('button-doUpdate').style.display = "none";

    clearForm();
}

// Show the table again
function showViewAll() {
    document.getElementById('button-showCreate').style.display = "block";
    document.getElementById('bookTable').style.display = "table";
    document.getElementById('createUpdateForm').style.display = "none";
}

// Clear the form
function clearForm() {
    let form = document.getElementById('createUpdateForm');
    form.querySelector('input[name="id"]').disabled = false;
    form.querySelector('input[name="id"]').value = "";
    form.querySelector('input[name="title"]').value = "";
    form.querySelector('input[name="author"]').value = "";
}

// Read book from form
function getBookFromForm() {
    let form = document.getElementById('createUpdateForm');
    let book = {};
    book.id = form.querySelector('input[name="id"]').value;
    book.title = form.querySelector('input[name="title"]').value;
    book.author = form.querySelector('input[name="author"]').value;
    return book;
}

// Add book to table
function addBookToTable(book) {
    let table = document.getElementById('bookTable');
    let row = table.insertRow(-1);

    row.setAttribute("id", book.id); // needed for update

    let cell1 = row.insertCell(0);
    cell1.textContent = book.id;

    let cell2 = row.insertCell(1);
    cell2.textContent = book.title;

    let cell3 = row.insertCell(2);
    cell3.textContent = book.author;

    let cell4 = row.insertCell(3);
    cell4.innerHTML = `
        <button onclick="showUpdate(this)">Update</button>
        <button onclick="doDelete(this)">Delete</button>
    `;
}

// Create
function doCreate() {
    let book = getBookFromForm();
    addBookToTable(book);
    clearForm();
    showViewAll();
}

// Read book from row
function getBookFromRow(row) {
    return {
        id: row.cells[0].textContent,
        title: row.cells[1].textContent,
        author: row.cells[2].textContent
    };
}

// Put book into form
function populateFormWithBook(book) {
    let form = document.getElementById('createUpdateForm');
    form.querySelector('input[name="id"]').disabled = true;
    form.querySelector('input[name="id"]').value = book.id;
    form.querySelector('input[name="title"]').value = book.title;
    form.querySelector('input[name="author"]').value = book.author;
}

// Show update form
function showUpdate(buttonElement) {
    showCreate(); // show form

    // switch to update mode
    document.getElementById('createLabel').style.display = "none";
    document.getElementById('updateLabel').style.display = "inline";
    document.getElementById('button-doCreate').style.display = "none";
    document.getElementById('button-doUpdate').style.display = "inline";

    let row = buttonElement.parentNode.parentNode;
    let book = getBookFromRow(row);
    populateFormWithBook(book);
}

// Update row
function setBookInRow(row, book) {
    row.cells[0].textContent = book.id;
    row.cells[1].textContent = book.title;
    row.cells[2].textContent = book.author;
}

// Do update
function doUpdate() {
    let book = getBookFromForm();
    let row = document.getElementById(book.id);
    setBookInRow(row, book);
    clearForm();
    showViewAll();
}

// Delete
function doDelete(buttonElement) {
    let row = buttonElement.parentNode.parentNode;
    row.parentNode.removeChild(row);
}
