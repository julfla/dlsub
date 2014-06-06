PREFIX = /usr
LD = ld
CC = cc
INSTALL = install
CFLAGS = -g -O2 -Wall -Wextra
LDFLAGS =
VLC_PLUGIN_CFLAGS := $(shell pkg-config --cflags vlc-plugin)
VLC_PLUGIN_LIBS := $(shell pkg-config --libs vlc-plugin)

libdir = $(PREFIX)/lib
plugindir = $(libdir)/vlc/plugins

override CC += -std=gnu99
override CPPFLAGS += -DPIC -I. -Isrc
override CFLAGS += -fPIC
override LDFLAGS += -Wl,-no-undefined,-z,defs

override CPPFLAGS += -DMODULE_STRING=\"foo\"
override CFLAGS += $(VLC_PLUGIN_CFLAGS)
override LDFLAGS += $(VLC_PLUGIN_LIBS)

TARGETS = libfoo_plugin.so

all: libfoo_plugin.so

install: all
		mkdir -p -- $(DESTDIR)$(plugindir)/misc
		$(INSTALL) --mode 0755 libfoo_plugin.so $(DESTDIR)$(plugindir)/misc

install-strip:
		$(MAKE) install INSTALL="$(INSTALL) -s"

uninstall:
		rm -f $(plugindir)/misc/libfoo_plugin.so

clean:
		rm -f -- libfoo_plugin.so src/*.o

mostlyclean: clean

SOURCES = foo.c

$(SOURCES:%.c=src/%.o): %: src/foo.h

libfoo_plugin.so: $(SOURCES:%.c=src/%.o)
		$(CC) $(LDFLAGS) -shared -o $@ $^

.PHONY: all install install-strip uninstall clean mostlyclean
