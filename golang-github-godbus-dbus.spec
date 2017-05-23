#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : golang-github-godbus-dbus
Version  : 5f6efc7ef2759c81b7ba876593971bfce311eab3
Release  : 6
URL      : https://github.com/godbus/dbus/archive/5f6efc7ef2759c81b7ba876593971bfce311eab3.tar.gz
Source0  : https://github.com/godbus/dbus/archive/5f6efc7ef2759c81b7ba876593971bfce311eab3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
BuildRequires : dbus
BuildRequires : dbus-extras
BuildRequires : go

%description
dbus
----
dbus is a simple library that implements native Go client bindings for the
D-Bus message bus system.

%prep
%setup -q -n dbus-5f6efc7ef2759c81b7ba876593971bfce311eab3

%build

%install
gopath="/usr/lib/golang"
library_path="github.com/godbus/dbus"
rm -rf %{buildroot}
install -d -p %{buildroot}${gopath}/src/${library_path}/
for file in $(find . -iname "*.go" -o -iname "*.h" -o -iname "*.c") ; do
     echo ${file}
     install -d -p %{buildroot}${gopath}/src/${library_path}/$(dirname $file)
     cp -pav $file %{buildroot}${gopath}/src/${library_path}/$file
done


%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/godbus/dbus/_examples/eavesdrop.go
/usr/lib/golang/src/github.com/godbus/dbus/_examples/introspect.go
/usr/lib/golang/src/github.com/godbus/dbus/_examples/list-names.go
/usr/lib/golang/src/github.com/godbus/dbus/_examples/notification.go
/usr/lib/golang/src/github.com/godbus/dbus/_examples/prop.go
/usr/lib/golang/src/github.com/godbus/dbus/_examples/server.go
/usr/lib/golang/src/github.com/godbus/dbus/_examples/signal.go
/usr/lib/golang/src/github.com/godbus/dbus/auth.go
/usr/lib/golang/src/github.com/godbus/dbus/auth_external.go
/usr/lib/golang/src/github.com/godbus/dbus/auth_sha1.go
/usr/lib/golang/src/github.com/godbus/dbus/call.go
/usr/lib/golang/src/github.com/godbus/dbus/conn.go
/usr/lib/golang/src/github.com/godbus/dbus/conn_darwin.go
/usr/lib/golang/src/github.com/godbus/dbus/conn_other.go
/usr/lib/golang/src/github.com/godbus/dbus/conn_test.go
/usr/lib/golang/src/github.com/godbus/dbus/dbus.go
/usr/lib/golang/src/github.com/godbus/dbus/decoder.go
/usr/lib/golang/src/github.com/godbus/dbus/doc.go
/usr/lib/golang/src/github.com/godbus/dbus/encoder.go
/usr/lib/golang/src/github.com/godbus/dbus/encoder_test.go
/usr/lib/golang/src/github.com/godbus/dbus/examples_test.go
/usr/lib/golang/src/github.com/godbus/dbus/export.go
/usr/lib/golang/src/github.com/godbus/dbus/export_test.go
/usr/lib/golang/src/github.com/godbus/dbus/homedir.go
/usr/lib/golang/src/github.com/godbus/dbus/homedir_dynamic.go
/usr/lib/golang/src/github.com/godbus/dbus/homedir_static.go
/usr/lib/golang/src/github.com/godbus/dbus/introspect/call.go
/usr/lib/golang/src/github.com/godbus/dbus/introspect/introspect.go
/usr/lib/golang/src/github.com/godbus/dbus/introspect/introspectable.go
/usr/lib/golang/src/github.com/godbus/dbus/message.go
/usr/lib/golang/src/github.com/godbus/dbus/object.go
/usr/lib/golang/src/github.com/godbus/dbus/prop/prop.go
/usr/lib/golang/src/github.com/godbus/dbus/proto_test.go
/usr/lib/golang/src/github.com/godbus/dbus/sig.go
/usr/lib/golang/src/github.com/godbus/dbus/sig_test.go
/usr/lib/golang/src/github.com/godbus/dbus/transport_darwin.go
/usr/lib/golang/src/github.com/godbus/dbus/transport_generic.go
/usr/lib/golang/src/github.com/godbus/dbus/transport_tcp.go
/usr/lib/golang/src/github.com/godbus/dbus/transport_tcp_test.go
/usr/lib/golang/src/github.com/godbus/dbus/transport_unix.go
/usr/lib/golang/src/github.com/godbus/dbus/transport_unix_test.go
/usr/lib/golang/src/github.com/godbus/dbus/transport_unixcred_dragonfly.go
/usr/lib/golang/src/github.com/godbus/dbus/transport_unixcred_linux.go
/usr/lib/golang/src/github.com/godbus/dbus/variant.go
/usr/lib/golang/src/github.com/godbus/dbus/variant_lexer.go
/usr/lib/golang/src/github.com/godbus/dbus/variant_parser.go
/usr/lib/golang/src/github.com/godbus/dbus/variant_test.go
