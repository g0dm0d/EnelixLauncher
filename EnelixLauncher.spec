# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['E:/GitClone/EnelixLauncher/launcher.py'],
             pathex=[],
             binaries=[],
             datas=[('E:/GitClone/EnelixLauncher/authAPI.py', '.'), ('E:/GitClone/EnelixLauncher/game.py', '.'), ('E:/GitClone/EnelixLauncher/UUID.py', '.'), ('E:/GitClone/EnelixLauncher/launcher.ui', '.'), ('E:/GitClone/EnelixLauncher/res/svg.png', '.')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          name='EnelixLauncher',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='E:\\GitClone\\EnelixLauncher\\icon.ico')