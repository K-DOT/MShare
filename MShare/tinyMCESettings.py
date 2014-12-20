TINYMCE_SETTINGS = {
    #'mode': "textareas",
    "mode" : "textareas",
    "theme" : "advanced",
    "language" : "ru",
    "inline_styles" : True,
    "convert_urls" : False,
    "relative_urls" : False,
    "remove_script_host" : False,
    "cleanup" : True,

    "extended_valid_elements" :
        """
            noindex, strong/b, em/i, sup, sub, ul, ol, li, div[class | id | style | name | title | align | width | height], span[class |
            id | style | name | title], hr[class | id | style | name | title | align | width | height], img[class | id | style | name | 
            title | src | align | alt | hspace | vspace | width | height | border=0], a[class | id | style | name | title | src | href | 
            rel | target | ], iframe[class | id | style | name | title | src | align | width | height | marginwidth | marginheight | scrolling 
            | frameborder | border | bordercolor],
            embed[class | id | style | name | title | align | width | height | hspace | vspace | type | pluginspage | src], object[class | id | style |
            name | title | align | width | height | hspace | vspace | type | classid | code | codebase | codetype | data]
        """,

    "plugins" : "pagebreak, style, layer, table, save, advhr, advimage, advlink, emotions, iespell, inlinepopups, insertdatetime, preview, media, searchreplace, print, contextmenu, paste, directionality, fullscreen, noneditable, visualchars, nonbreaking, xhtmlxtras, template, wordcount, advlist, autosave""",
    #Theme options
    "theme_advanced_buttons1" : """undo, redo, |, bold, italic, underline, strikethrough, |, justifyleft, justifycenter, justifyright, justifyfull, styleselect, formatselect, fontselect, fontsizeselect, sub, sup, |, forecolor, backcolor""",
    "theme_advanced_buttons2" : """cut, copy, paste, pastetext, pasteword, removeformat, cleanup, |, search, replace, |, bullist, numlist, |, outdent, indent, blockquote, |, link, unlink, image, |, insertdate, inserttime, hr, |, charmap, emotions, iespell""",
    "theme_advanced_buttons3" : """tablecontrols, |, visualaid""",
    "theme_advanced_buttons4" : """styleprops, |, cite, abbr, acronym, del, ins, |, visualchars, nonbreaking, |, print, preview, |, fullscreen""",
    "theme_advanced_toolbar_location" : "top",
    "theme_advanced_toolbar_align" : "left",
    "theme_advanced_statusbar_location" : "bottom",
    "theme_advanced_resizing" : True,


    'width': '600',
    'height': '400'
}