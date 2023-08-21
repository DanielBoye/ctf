function createSuccessMessage(msg)
{
    const container = $("<div class='alert alert-dismissible alert-success'>" +
                    "<button type='button' class='close' data-dismiss='alert'>&times;</button>" +
                    "<strong>SUCCESS!</strong> " + 
                "</div>")
    container.append(document.createTextNode(msg))

    return container
}

function createErrorMessage(msg)
{
    const container = $("<div class='alert alert-dismissible alert-danger'>" +
                    "<button type='button' class='close' data-dismiss='alert'>&times;</button>" +
                    "<strong>ERROR!</strong> " + 
                "</div>")
    container.append(document.createTextNode(msg))

    return container
}

function clearMessages()
{
    $(".alert").remove()
}