# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['E:\\HNU\\\xc8\xed\xbc\xfe\xb9\xa4\xb3\xcc\\\xbd\xf0\xc8\xda\\\xb7\xd6\xce\xf6'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='main',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
