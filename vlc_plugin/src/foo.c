#include "foo.h"
#include <stdio.h>
#include <stdlib.h>
#include <vlc_common.h>
#include <vlc_plugin.h>
#include <vlc_stream.h>

#define DOMAIN  "foo"
#define MODULE_STRING "foo"

static int  Open(vlc_object_t *obj);
static void Close(vlc_object_t *obj);

vlc_module_begin()
    set_category(CAT_INPUT)
    set_subcategory(SUBCAT_INPUT_SCODEC)
    set_shortname("foo")
    set_description("A sample interface.")
    set_capability("interface", 0)
    set_callbacks(Open, Close)
vlc_module_end()

static int Open(vlc_object_t *obj) {
     printf("\n\nOpen of my sample interface....\n");
    return VLC_SUCCESS;
}

static void Close(vlc_object_t *obj) {
    printf("\n\nClose of sample interface\n\n");
}
