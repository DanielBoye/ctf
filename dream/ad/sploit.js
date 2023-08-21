// Overview of sploits - list.html
$(function(){
    function patch(sploit, version, enable){
        const action = document.createElement("input")
        action.setAttribute("type", "hidden")
        action.setAttribute("name", "enabled")
        action.setAttribute("value", enable ? 1 : 0)

        const form = document.createElement("form")
        form.setAttribute("action", '/ui/sploits/' + encodeURIComponent(sploit) + "/" + encodeURIComponent(version))
        form.setAttribute("method", "POST")
        form.appendChild(action)

        document.body.appendChild(form)
        form.submit()
    }

    $(document).on("click", ".btn-sploit-activate", (e, elm) => {
        const sploit = $(e.target).data("sploit")
        const version = $(e.target).data("version")

        patch(sploit, version, true)
    })

    $(document).on("click", ".btn-sploit-deactivate", (e, elm) => {
        const sploit = $(e.target).data("sploit")
        const version = $(e.target).data("version")

        patch(sploit, version, false)
    })
})

// Sploit editor - editor.html
$(function(){
    const submitBtn = $("#editor [type=submit]")
    const originalSubmitText = submitBtn.text()

    const disableSubmitButton = () => {
        submitBtn
        .prop("disabled", true)
        .text("Saving...")
    }

    const restoreSubmitButton = () => {
        submitBtn
            .text(originalSubmitText)
            .prop("disabled", false)
    } 

    $("#editor").submit(e => {
        e.preventDefault()

        disableSubmitButton()
        clearMessages()

        const form = e.target

        $.post('/ui/sploits/' + encodeURIComponent(form.filename.value), {
            code: form.code.value,
            version: form.version.value
        }, "json")
            .fail(() => {
                $(form).prepend(createErrorMessage("Could not save your script!"))
            })
            .done((d) => {
                if(d.error){
                    $(form).prepend(createErrorMessage(d.error))
                } else if(!d.success){
                    $(form).prepend(createErrorMessage("Could not save your script! Got an unknown error!"))
                } else {
                    form.version.value = d.version

                    const time = new Date().toTimeString().split(" ")[0]
                    $(form).prepend(createSuccessMessage(`Sploit saved at ${time}!`))
                }
            })
            .always(restoreSubmitButton)
    })

    $(".btn-fetch-log").click(e => {
        e.preventDefault()
        clearMessages()

        const elm = $(e.target)
        const container = elm.closest(".log-container")
        const filename = elm.data("sploit")

        $.get('/ui/sploits/' + encodeURIComponent(filename) + "/log")
        .fail(() => {
            $(container).prepend(createErrorMessage("Could not fetch latest log contents"))
        })
        .done(out => {
            const log = $(container).find(".log-output")
            log.val(out)
            log.scrollTop(log[0].scrollHeight);
        })
    })
    .trigger("click")
})