# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['mikochiku_alarm.py'],
             pathex=['.\\'],
             binaries=[],
             datas=[
                ('icon.ico','.'), 
                ('alarm.mp3','.'),
                ('lang/*','lang'),
                ('channel/*','channel')
             ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='mikochiku_alarm',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,icon="icon.ico" )

