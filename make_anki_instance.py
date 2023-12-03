from pathlib import Path

name = input('Enter name of user: ')

app_name = name + 'Anki'

app_dir = Path('~/Applications').expanduser() / (app_name + '.app')

app_dir.mkdir()

contents_dir = app_dir / 'Contents'
contents_dir.mkdir()

info_file = contents_dir / 'Info.plist'
info_file.write_text(f"""\
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>CFBundleExecutable</key>
    <string>{app_name}</string>
    <key>CFBundleGetInfoString</key>
    <string>{app_name} 1.0</string>
    <key>CFBundleVersion</key>
    <string>1.0</string>
    <key>CFBundleShortVersionString</key>
    <string>1.0</string>
  </dict>
</plist>
""")

macos_dir = app_dir / 'Contents' / 'MacOS'
macos_dir.mkdir(parents=True)

shell_file = macos_dir / app_name
shell_file.write_text(f"""\
#!/bin/bash
open -a Anki --args -b {app_dir / 'data'}
""")
shell_file.chmod(0o755)
