  Fixed this by installing python-dotenv rather than dotenv
  You can still import dotenv using this method as they are the same module.
  
  WARNING: Discarding https://files.pythonhosted.org/packages/20/e0/6c03055f8520384b0050bb97757ab58afae5f35adb8b9a26bba2cd4de8bd/distribute-0.6.16.tar.gz#sha256=cb2de242f3af2d1aa225e514e5b8ed7d41cdb4c505d3cf5cc6e3ca0646b4dd9b (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
        ERROR: Command errored out with exit status 1:
         command: '/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_d232ce0800204366a78d64569ba6dffa/setup.py'"'"'; __file__='"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_d232ce0800204366a78d64569ba6dffa/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-pip-egg-info-w2501sh_
             cwd: /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_d232ce0800204366a78d64569ba6dffa/
        Complete output (15 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_d232ce0800204366a78d64569ba6dffa/setuptools/__init__.py", line 2, in <module>
            from setuptools.extension import Extension, Library
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_d232ce0800204366a78d64569ba6dffa/setuptools/extension.py", line 2, in <module>
            from setuptools.dist import _get_unpatched
          File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
          File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
          File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/_virtualenv.py", line 89, in exec_module
            old(module)
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_d232ce0800204366a78d64569ba6dffa/setuptools/dist.py", line 103
            except ValueError, e:
                             ^
        SyntaxError: invalid syntax
        ----------------------------------------
    WARNING: Discarding https://files.pythonhosted.org/packages/7f/00/9219235d4222c3da6729e6e2afa4a9080b987169bab3b2ec6cbb7c2e86da/distribute-0.6.15.zip#sha256=a6cba0f43a70dceab680ba475df2a451b53257e5dc3267323c2a666c1673a31b (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
        ERROR: Command errored out with exit status 1:
         command: '/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_9752cc03c6a64497996f6b4edf9d71cb/setup.py'"'"'; __file__='"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_9752cc03c6a64497996f6b4edf9d71cb/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-pip-egg-info-nxz2uld4
             cwd: /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_9752cc03c6a64497996f6b4edf9d71cb/
        Complete output (15 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_9752cc03c6a64497996f6b4edf9d71cb/setuptools/__init__.py", line 2, in <module>
            from setuptools.extension import Extension, Library
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_9752cc03c6a64497996f6b4edf9d71cb/setuptools/extension.py", line 2, in <module>
            from setuptools.dist import _get_unpatched
          File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
          File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
          File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/_virtualenv.py", line 89, in exec_module
            old(module)
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_9752cc03c6a64497996f6b4edf9d71cb/setuptools/dist.py", line 103
            except ValueError, e:
                             ^
        SyntaxError: invalid syntax
        ----------------------------------------
    WARNING: Discarding https://files.pythonhosted.org/packages/07/a6/8f6b270b7e6a1be3df78b174e2437fdb631cfcce16f82c2f8b7affb50ee2/distribute-0.6.15.tar.gz#sha256=85b05942f84146d8f0ed17906b90af7662d649b922fe77a8c402da5da258a481 (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
        ERROR: Command errored out with exit status 1:
         command: '/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_c27cc9931b614f27adb8577b5cddd890/setup.py'"'"'; __file__='"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_c27cc9931b614f27adb8577b5cddd890/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-pip-egg-info-cd68ftot
             cwd: /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_c27cc9931b614f27adb8577b5cddd890/
        Complete output (15 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_c27cc9931b614f27adb8577b5cddd890/setuptools/__init__.py", line 2, in <module>
            from setuptools.extension import Extension, Library
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_c27cc9931b614f27adb8577b5cddd890/setuptools/extension.py", line 2, in <module>
            from setuptools.dist import _get_unpatched
          File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
          File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
          File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/_virtualenv.py", line 89, in exec_module
            old(module)
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_c27cc9931b614f27adb8577b5cddd890/setuptools/dist.py", line 103
            except ValueError, e:
                             ^
        SyntaxError: invalid syntax
        ----------------------------------------
    WARNING: Discarding https://files.pythonhosted.org/packages/0b/f7/c564907eacadc3cbace0174a95c9176e5a371e19ddc38baf1919d2d8cb3d/distribute-0.6.14.zip#sha256=4ceec6b1ec8300fe4e1a60a9781c7bc1956feee0d6a87a002254aca080a9126d (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
        ERROR: Command errored out with exit status 1:
         command: '/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_a10c1e3846a245bc97d7b9b8823bd105/setup.py'"'"'; __file__='"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_a10c1e3846a245bc97d7b9b8823bd105/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-pip-egg-info-p27nitzp
             cwd: /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_a10c1e3846a245bc97d7b9b8823bd105/
        Complete output (15 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_a10c1e3846a245bc97d7b9b8823bd105/setuptools/__init__.py", line 2, in <module>
            from setuptools.extension import Extension, Library
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_a10c1e3846a245bc97d7b9b8823bd105/setuptools/extension.py", line 2, in <module>
            from setuptools.dist import _get_unpatched
          File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
          File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
          File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/_virtualenv.py", line 89, in exec_module
            old(module)
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_a10c1e3846a245bc97d7b9b8823bd105/setuptools/dist.py", line 103
            except ValueError, e:
                             ^
        SyntaxError: invalid syntax
        ----------------------------------------
    WARNING: Discarding https://files.pythonhosted.org/packages/95/f1/6128255a94f3d57e0f7ec2767c1893d1ab769bef48e847173f923d977e1d/distribute-0.6.14.tar.gz#sha256=44c92b7edbc0ff9cd5847291e7dcb4cc75e24247a306bd4b8a139abd355b0db0 (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
        ERROR: Command errored out with exit status 1:
         command: '/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_a920704129c34689bad698867fdba906/setup.py'"'"'; __file__='"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_a920704129c34689bad698867fdba906/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-pip-egg-info-nvr9z9ai
             cwd: /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_a920704129c34689bad698867fdba906/
        Complete output (15 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_a920704129c34689bad698867fdba906/setuptools/__init__.py", line 2, in <module>
            from setuptools.extension import Extension, Library
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_a920704129c34689bad698867fdba906/setuptools/extension.py", line 2, in <module>
            from setuptools.dist import _get_unpatched
          File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
          File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
          File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/_virtualenv.py", line 89, in exec_module
            old(module)
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_a920704129c34689bad698867fdba906/setuptools/dist.py", line 103
            except ValueError, e:
                             ^
        SyntaxError: invalid syntax
        ----------------------------------------
    WARNING: Discarding https://files.pythonhosted.org/packages/c6/4c/0ba3f3d7075381526f15a47ce7835e5d1577caec569cc29653dfa0231350/distribute-0.6.13.zip#sha256=4b935edc3bd049cc4c597c123e515d428619a8c8b0b477cbe95343cb479ba3a8 (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
        ERROR: Command errored out with exit status 1:
         command: '/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_e4b53d1dee7a4ca184dcca26e26571cd/setup.py'"'"'; __file__='"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_e4b53d1dee7a4ca184dcca26e26571cd/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-pip-egg-info-qnib0dgu
             cwd: /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_e4b53d1dee7a4ca184dcca26e26571cd/
        Complete output (15 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_e4b53d1dee7a4ca184dcca26e26571cd/setuptools/__init__.py", line 2, in <module>
            from setuptools.extension import Extension, Library
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_e4b53d1dee7a4ca184dcca26e26571cd/setuptools/extension.py", line 2, in <module>
            from setuptools.dist import _get_unpatched
          File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
          File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
          File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/_virtualenv.py", line 89, in exec_module
            old(module)
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_e4b53d1dee7a4ca184dcca26e26571cd/setuptools/dist.py", line 103
            except ValueError, e:
                             ^
        SyntaxError: invalid syntax
        ----------------------------------------
    WARNING: Discarding https://files.pythonhosted.org/packages/0b/89/94f3ecf6767ee521962c3b128ef832d452f9b857b244bebfb0b8426d909f/distribute-0.6.13.tar.gz#sha256=a4acfcbd37741ea5ae9510ec72a8e8c482d7d4a504cba3d72ecd3971165d7e85 (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
        ERROR: Command errored out with exit status 1:
         command: '/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_6812a30a059a42afbbd007baa8b6ba06/setup.py'"'"'; __file__='"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_6812a30a059a42afbbd007baa8b6ba06/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-pip-egg-info-3cdinmm8
             cwd: /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_6812a30a059a42afbbd007baa8b6ba06/
        Complete output (15 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_6812a30a059a42afbbd007baa8b6ba06/setuptools/__init__.py", line 2, in <module>
            from setuptools.extension import Extension, Library
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_6812a30a059a42afbbd007baa8b6ba06/setuptools/extension.py", line 2, in <module>
            from setuptools.dist import _get_unpatched
          File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
          File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
          File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/_virtualenv.py", line 89, in exec_module
            old(module)
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_6812a30a059a42afbbd007baa8b6ba06/setuptools/dist.py", line 103
            except ValueError, e:
                             ^
        SyntaxError: invalid syntax
        ----------------------------------------
    WARNING: Discarding https://files.pythonhosted.org/packages/42/71/9dfd846af8d66f94ef3b32fa9c36de7d2303e6080ec21f12d9a38c72287a/distribute-0.6.12.zip#sha256=06382930f84acc74d8dd9d15c30bdfa378532b0e6c65f391dff4d310dd0b14ea (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
        ERROR: Command errored out with exit status 1:
         command: '/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_be87dbf9d5f547008139605ebb332950/setup.py'"'"'; __file__='"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_be87dbf9d5f547008139605ebb332950/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-pip-egg-info-qo2t3dx7
             cwd: /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_be87dbf9d5f547008139605ebb332950/
        Complete output (15 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_be87dbf9d5f547008139605ebb332950/setuptools/__init__.py", line 2, in <module>
            from setuptools.extension import Extension, Library
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_be87dbf9d5f547008139605ebb332950/setuptools/extension.py", line 2, in <module>
            from setuptools.dist import _get_unpatched
          File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
          File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
          File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/_virtualenv.py", line 89, in exec_module
            old(module)
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_be87dbf9d5f547008139605ebb332950/setuptools/dist.py", line 103
            except ValueError, e:
                             ^
        SyntaxError: invalid syntax
        ----------------------------------------
    WARNING: Discarding https://files.pythonhosted.org/packages/cd/fb/efc926f7231e011d2abedf7cb3835dfccf2d5e08fa115a30fe9225244bb3/distribute-0.6.12.tar.gz#sha256=a519e9e6a402be4d206d934885bf263f47adf1e88084eeffc3fa00fe64133a45 (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
        ERROR: Command errored out with exit status 1:
         command: '/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_b2c03c8b4dad4b7bb0e14a11d16e805d/setup.py'"'"'; __file__='"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_b2c03c8b4dad4b7bb0e14a11d16e805d/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-pip-egg-info-4_ua9qqc
             cwd: /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_b2c03c8b4dad4b7bb0e14a11d16e805d/
        Complete output (15 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_b2c03c8b4dad4b7bb0e14a11d16e805d/setuptools/__init__.py", line 2, in <module>
            from setuptools.extension import Extension, Library
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_b2c03c8b4dad4b7bb0e14a11d16e805d/setuptools/extension.py", line 2, in <module>
            from setuptools.dist import _get_unpatched
          File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
          File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
          File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/_virtualenv.py", line 89, in exec_module
            old(module)
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_b2c03c8b4dad4b7bb0e14a11d16e805d/setuptools/dist.py", line 103
            except ValueError, e:
                             ^
        SyntaxError: invalid syntax
        ----------------------------------------
    WARNING: Discarding https://files.pythonhosted.org/packages/aa/37/86c4925d9fd77500599d29325f07e0c1ccd6b6bf9150a06144e7604b5c9e/distribute-0.6.11.zip#sha256=e35c3554fa5f66013ab5be1f3387146c565ec028514733d571cc6f42e1af0e1f (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
        ERROR: Command errored out with exit status 1:
         command: '/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_5b9ad4e075fc4a48b3de5de8e8baa577/setup.py'"'"'; __file__='"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_5b9ad4e075fc4a48b3de5de8e8baa577/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-pip-egg-info-5a43ldf1
             cwd: /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_5b9ad4e075fc4a48b3de5de8e8baa577/
        Complete output (15 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_5b9ad4e075fc4a48b3de5de8e8baa577/setuptools/__init__.py", line 2, in <module>
            from setuptools.extension import Extension, Library
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_5b9ad4e075fc4a48b3de5de8e8baa577/setuptools/extension.py", line 2, in <module>
            from setuptools.dist import _get_unpatched
          File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
          File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
          File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/_virtualenv.py", line 89, in exec_module
            old(module)
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_5b9ad4e075fc4a48b3de5de8e8baa577/setuptools/dist.py", line 103
            except ValueError, e:
                             ^
        SyntaxError: invalid syntax
        ----------------------------------------
    WARNING: Discarding https://files.pythonhosted.org/packages/60/6b/a6b6a5bfd5a04ba71a458fe50c86d10855cf3ccc04ec11a3f2b94681c67b/distribute-0.6.11.tar.gz#sha256=d04390637087e25dfc0851d0c352900b64c0cf9b831d40e89de5636ec3df8bee (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
        ERROR: Command errored out with exit status 1:
         command: '/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_2555f79a4190475bae323dfb5cb1528f/setup.py'"'"'; __file__='"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_2555f79a4190475bae323dfb5cb1528f/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-pip-egg-info-eyi7fohh
             cwd: /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_2555f79a4190475bae323dfb5cb1528f/
        Complete output (15 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_2555f79a4190475bae323dfb5cb1528f/setuptools/__init__.py", line 2, in <module>
            from setuptools.extension import Extension, Library
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_2555f79a4190475bae323dfb5cb1528f/setuptools/extension.py", line 2, in <module>
            from setuptools.dist import _get_unpatched
          File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
          File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
          File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/_virtualenv.py", line 89, in exec_module
            old(module)
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_2555f79a4190475bae323dfb5cb1528f/setuptools/dist.py", line 103
            except ValueError, e:
                             ^
        SyntaxError: invalid syntax
        ----------------------------------------
    WARNING: Discarding https://files.pythonhosted.org/packages/39/19/dae27189d9c1758e3db9bf27930e88cc05b0ca60c3eb5668ca6e329a6fca/distribute-0.6.10.zip#sha256=ccaec91646cd6a57eae7aecc9c819fd8300c8d0005019a2ce7485e572ab485dd (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
        ERROR: Command errored out with exit status 1:
         command: '/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_071920eb52a24e30847f74c7bd496dd8/setup.py'"'"'; __file__='"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_071920eb52a24e30847f74c7bd496dd8/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-pip-egg-info-4yovt6vb
             cwd: /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_071920eb52a24e30847f74c7bd496dd8/
        Complete output (15 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_071920eb52a24e30847f74c7bd496dd8/setuptools/__init__.py", line 2, in <module>
            from setuptools.extension import Extension, Library
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_071920eb52a24e30847f74c7bd496dd8/setuptools/extension.py", line 2, in <module>
            from setuptools.dist import _get_unpatched
          File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
          File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
          File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/_virtualenv.py", line 89, in exec_module
            old(module)
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_071920eb52a24e30847f74c7bd496dd8/setuptools/dist.py", line 103
            except ValueError, e:
                             ^
        SyntaxError: invalid syntax
        ----------------------------------------
    WARNING: Discarding https://files.pythonhosted.org/packages/07/9d/2af576b8b199c69d839a8dfd6025b6721a18a0b771a051b2b62b3c866d0f/distribute-0.6.10.tar.gz#sha256=0c291a31248376ca76b5662c6ff4e33e7d3eba6d91b4c0a5ca663c9c954e8a1a (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
        ERROR: Command errored out with exit status 1:
         command: '/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_e40f0e8efe1b406ebe683f8a27987715/setup.py'"'"'; __file__='"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_e40f0e8efe1b406ebe683f8a27987715/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-pip-egg-info-b482a4r0
             cwd: /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_e40f0e8efe1b406ebe683f8a27987715/
        Complete output (15 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_e40f0e8efe1b406ebe683f8a27987715/setuptools/__init__.py", line 2, in <module>
            from setuptools.extension import Extension, Library
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_e40f0e8efe1b406ebe683f8a27987715/setuptools/extension.py", line 2, in <module>
            from setuptools.dist import _get_unpatched
          File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
          File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
          File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/_virtualenv.py", line 89, in exec_module
            old(module)
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_e40f0e8efe1b406ebe683f8a27987715/setuptools/dist.py", line 103
            except ValueError, e:
                             ^
        SyntaxError: invalid syntax
        ----------------------------------------
    WARNING: Discarding https://files.pythonhosted.org/packages/e8/1f/746778ad7044fe4767a3e3122ad75d0487441342ae00940d2b333f53c03f/distribute-0.6.9.zip#sha256=e2f411eda7535eb7af0cc032c6e104733c3d3afbd7d79de25b925d740eb9cbd4 (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
        ERROR: Command errored out with exit status 1:
         command: '/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_c53ed1952f6546d2b3a5fe540673b79c/setup.py'"'"'; __file__='"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_c53ed1952f6546d2b3a5fe540673b79c/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-pip-egg-info-ndr2udfv
             cwd: /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_c53ed1952f6546d2b3a5fe540673b79c/
        Complete output (15 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_c53ed1952f6546d2b3a5fe540673b79c/setuptools/__init__.py", line 2, in <module>
            from setuptools.extension import Extension, Library
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_c53ed1952f6546d2b3a5fe540673b79c/setuptools/extension.py", line 2, in <module>
            from setuptools.dist import _get_unpatched
          File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
          File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
          File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/_virtualenv.py", line 89, in exec_module
            old(module)
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_c53ed1952f6546d2b3a5fe540673b79c/setuptools/dist.py", line 103
            except ValueError, e:
                             ^
        SyntaxError: invalid syntax
        ----------------------------------------
    WARNING: Discarding https://files.pythonhosted.org/packages/a9/a1/06b34f4fa52e35059f582572f7de5592744897f88ac488c97a715bfa71c9/distribute-0.6.9.tar.gz#sha256=aa59755d040a466fc0bb5b15f5a7ae711994a39723ab23a3b75fa4dcc4986543 (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
        ERROR: Command errored out with exit status 1:
         command: '/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_3aad9b1148164063a48d056be147d06e/setup.py'"'"'; __file__='"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_3aad9b1148164063a48d056be147d06e/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-pip-egg-info-cmhhzfrk
             cwd: /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_3aad9b1148164063a48d056be147d06e/
        Complete output (15 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_3aad9b1148164063a48d056be147d06e/setuptools/__init__.py", line 2, in <module>
            from setuptools.extension import Extension, Library
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_3aad9b1148164063a48d056be147d06e/setuptools/extension.py", line 2, in <module>
            from setuptools.dist import _get_unpatched
          File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
          File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
          File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/_virtualenv.py", line 89, in exec_module
            old(module)
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_3aad9b1148164063a48d056be147d06e/setuptools/dist.py", line 103
            except ValueError, e:
                             ^
        SyntaxError: invalid syntax
        ----------------------------------------
    WARNING: Discarding https://files.pythonhosted.org/packages/f2/ea/f708dba54ba7ad36d6b032554cc45d2ded60df8f806387aff7ea89dfa028/distribute-0.6.8.zip#sha256=781a6f1ba19d85d7067b919a6b31b8fff6d0f513581f7586eac60480be0277ce (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
        ERROR: Command errored out with exit status 1:
         command: '/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_e2afc77d342f4a898491b860a8990d62/setup.py'"'"'; __file__='"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_e2afc77d342f4a898491b860a8990d62/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-pip-egg-info-kdzxllb3
             cwd: /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_e2afc77d342f4a898491b860a8990d62/
        Complete output (15 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_e2afc77d342f4a898491b860a8990d62/setuptools/__init__.py", line 2, in <module>
            from setuptools.extension import Extension, Library
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_e2afc77d342f4a898491b860a8990d62/setuptools/extension.py", line 2, in <module>
            from setuptools.dist import _get_unpatched
          File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
          File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
          File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/_virtualenv.py", line 89, in exec_module
            old(module)
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_e2afc77d342f4a898491b860a8990d62/setuptools/dist.py", line 103
            except ValueError, e:
                             ^
        SyntaxError: invalid syntax
        ----------------------------------------
    WARNING: Discarding https://files.pythonhosted.org/packages/f3/ae/7a31bd7a09548f3fc57408837b4a183ff48e60085b5d0f08026e375ebbd0/distribute-0.6.8.tar.gz#sha256=f75b3a011be311186d1bddfb3cc1767537eb35332fbf1fc19309dd36ebc737bf (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
        ERROR: Command errored out with exit status 1:
         command: '/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_1b6b2e850c6147b29da9f4753a0c01f0/setup.py'"'"'; __file__='"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_1b6b2e850c6147b29da9f4753a0c01f0/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-pip-egg-info-_bfbou12
             cwd: /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_1b6b2e850c6147b29da9f4753a0c01f0/
        Complete output (15 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_1b6b2e850c6147b29da9f4753a0c01f0/setuptools/__init__.py", line 2, in <module>
            from setuptools.extension import Extension, Library
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_1b6b2e850c6147b29da9f4753a0c01f0/setuptools/extension.py", line 2, in <module>
            from setuptools.dist import _get_unpatched
          File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
          File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
          File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/_virtualenv.py", line 89, in exec_module
            old(module)
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_1b6b2e850c6147b29da9f4753a0c01f0/setuptools/dist.py", line 102
            except ValueError, e:
                             ^
        SyntaxError: invalid syntax
        ----------------------------------------
    WARNING: Discarding https://files.pythonhosted.org/packages/0d/7e/82122b2b6371655491ec668737daf5b278efaab082de13adbd100207f6b9/distribute-0.6.7.zip#sha256=c8ea44c881a0a0c2f29e506800abfa236ea0704dc565ce19c436fd7912952025 (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
        ERROR: Command errored out with exit status 1:
         command: '/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_6d117740b95a4309b24c8a4d20520ade/setup.py'"'"'; __file__='"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_6d117740b95a4309b24c8a4d20520ade/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-pip-egg-info-2tapd7b_
             cwd: /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_6d117740b95a4309b24c8a4d20520ade/
        Complete output (15 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_6d117740b95a4309b24c8a4d20520ade/setuptools/__init__.py", line 2, in <module>
            from setuptools.extension import Extension, Library
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_6d117740b95a4309b24c8a4d20520ade/setuptools/extension.py", line 2, in <module>
            from setuptools.dist import _get_unpatched
          File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
          File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
          File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/_virtualenv.py", line 89, in exec_module
            old(module)
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_6d117740b95a4309b24c8a4d20520ade/setuptools/dist.py", line 102
            except ValueError, e:
                             ^
        SyntaxError: invalid syntax
        ----------------------------------------
    WARNING: Discarding https://files.pythonhosted.org/packages/c9/db/1c44a07d77ea84886f666a6201db043e979f94c990e6e796e0cf4d57c63d/distribute-0.6.7.tar.gz#sha256=0ad2916d5821a2b8adecee3bd2ff03399f7ebe69a7eab2341528089c1e4b77ca (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
        ERROR: Command errored out with exit status 1:
         command: '/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_cdd94714ade543cbbdd450d1288fa0d3/setup.py'"'"'; __file__='"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_cdd94714ade543cbbdd450d1288fa0d3/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-pip-egg-info-_b8_yxc3
             cwd: /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_cdd94714ade543cbbdd450d1288fa0d3/
        Complete output (15 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_cdd94714ade543cbbdd450d1288fa0d3/setuptools/__init__.py", line 2, in <module>
            from setuptools.extension import Extension, Library
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_cdd94714ade543cbbdd450d1288fa0d3/setuptools/extension.py", line 2, in <module>
            from setuptools.dist import _get_unpatched
          File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
          File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
          File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/_virtualenv.py", line 89, in exec_module
            old(module)
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_cdd94714ade543cbbdd450d1288fa0d3/setuptools/dist.py", line 102
            except ValueError, e:
                             ^
        SyntaxError: invalid syntax
        ----------------------------------------
    WARNING: Discarding https://files.pythonhosted.org/packages/dd/34/01ceefc58caf5e1b4be0fc917b539bf456c78b77005d201a10306372dddf/distribute-0.6.6.zip#sha256=b6c545bf6d1ac79ad73ff8d3fb8a6e9cf25bd7393f1cd93d617128cef3d08ecd (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
        ERROR: Command errored out with exit status 1:
         command: '/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_de974e7308af471f9c2238e251f28978/setup.py'"'"'; __file__='"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_de974e7308af471f9c2238e251f28978/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-pip-egg-info-om7ojc7j
             cwd: /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_de974e7308af471f9c2238e251f28978/
        Complete output (15 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_de974e7308af471f9c2238e251f28978/setuptools/__init__.py", line 2, in <module>
            from setuptools.extension import Extension, Library
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_de974e7308af471f9c2238e251f28978/setuptools/extension.py", line 2, in <module>
            from setuptools.dist import _get_unpatched
          File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
          File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
          File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/_virtualenv.py", line 89, in exec_module
            old(module)
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_de974e7308af471f9c2238e251f28978/setuptools/dist.py", line 102
            except ValueError, e:
                             ^
        SyntaxError: invalid syntax
        ----------------------------------------
    WARNING: Discarding https://files.pythonhosted.org/packages/f0/f3/f020debdcd692437d235a93194c649273d6a46d815254c366cbf4ed9e029/distribute-0.6.6.tar.gz#sha256=ca9fcf7477d655f4e72ddbe1a15d1aacb066462e77ff5af0654eeda2c777c922 (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
        ERROR: Command errored out with exit status 1:
         command: '/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_083d221c05934f87870403d6ed91fe82/setup.py'"'"'; __file__='"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_083d221c05934f87870403d6ed91fe82/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-pip-egg-info-tmsdnfav
             cwd: /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_083d221c05934f87870403d6ed91fe82/
        Complete output (15 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_083d221c05934f87870403d6ed91fe82/setuptools/__init__.py", line 2, in <module>
            from setuptools.extension import Extension, Library
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_083d221c05934f87870403d6ed91fe82/setuptools/extension.py", line 2, in <module>
            from setuptools.dist import _get_unpatched
          File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
          File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
          File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/_virtualenv.py", line 89, in exec_module
            old(module)
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_083d221c05934f87870403d6ed91fe82/setuptools/dist.py", line 102
            except ValueError, e:
                             ^
        SyntaxError: invalid syntax
        ----------------------------------------
    WARNING: Discarding https://files.pythonhosted.org/packages/b1/de/0332e445bdbb7022852d5a2435c064c167fc4943b76383ad4e30a9d7ca07/distribute-0.6.5.zip#sha256=659461027e71c0e501c033a6dd07fd3eda2e68bf4211af8c38ac3062d5f5c6a4 (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
        ERROR: Command errored out with exit status 1:
         command: '/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_b2e5a9d0ac10464fb4f5ebcf629c88e2/setup.py'"'"'; __file__='"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_b2e5a9d0ac10464fb4f5ebcf629c88e2/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-pip-egg-info-94pqawnj
             cwd: /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_b2e5a9d0ac10464fb4f5ebcf629c88e2/
        Complete output (15 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_b2e5a9d0ac10464fb4f5ebcf629c88e2/setuptools/__init__.py", line 2, in <module>
            from setuptools.extension import Extension, Library
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_b2e5a9d0ac10464fb4f5ebcf629c88e2/setuptools/extension.py", line 2, in <module>
            from setuptools.dist import _get_unpatched
          File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
          File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
          File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/_virtualenv.py", line 89, in exec_module
            old(module)
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_b2e5a9d0ac10464fb4f5ebcf629c88e2/setuptools/dist.py", line 102
            except ValueError, e:
                             ^
        SyntaxError: invalid syntax
        ----------------------------------------
    WARNING: Discarding https://files.pythonhosted.org/packages/2a/cd/71002045b4ba17c96e5965459216962bf0a1d2e11262b0831e0abb021d23/distribute-0.6.5.tar.gz#sha256=e97fea8207f09ef729f21ae2be49a0692d5e0f169945ee89113dbcc0efcd8c4d (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
        ERROR: Command errored out with exit status 1:
         command: '/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_e8f47aa3a0c241ebacc1730cd1f55d4d/setup.py'"'"'; __file__='"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_e8f47aa3a0c241ebacc1730cd1f55d4d/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-pip-egg-info-1kh6phuj
             cwd: /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_e8f47aa3a0c241ebacc1730cd1f55d4d/
        Complete output (15 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_e8f47aa3a0c241ebacc1730cd1f55d4d/setuptools/__init__.py", line 2, in <module>
            from setuptools.extension import Extension, Library
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_e8f47aa3a0c241ebacc1730cd1f55d4d/setuptools/extension.py", line 2, in <module>
            from setuptools.dist import _get_unpatched
          File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
          File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
          File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/_virtualenv.py", line 89, in exec_module
            old(module)
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_e8f47aa3a0c241ebacc1730cd1f55d4d/setuptools/dist.py", line 102
            except ValueError, e:
                             ^
        SyntaxError: invalid syntax
        ----------------------------------------
    WARNING: Discarding https://files.pythonhosted.org/packages/bd/98/111ba95670f9786ba7ef9bb600f250c927335a8cc4033cd54e56762e2979/distribute-0.6.4.zip#sha256=ce60933f17febe26528b62609b922db4301d4c8d25f02fac155cae339dd1eb12 (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
        ERROR: Command errored out with exit status 1:
         command: '/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_dc5a6011e02d4c70ad915109965f64c5/setup.py'"'"'; __file__='"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_dc5a6011e02d4c70ad915109965f64c5/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-pip-egg-info-1exis45b
             cwd: /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_dc5a6011e02d4c70ad915109965f64c5/
        Complete output (15 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_dc5a6011e02d4c70ad915109965f64c5/setuptools/__init__.py", line 2, in <module>
            from setuptools.extension import Extension, Library
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_dc5a6011e02d4c70ad915109965f64c5/setuptools/extension.py", line 2, in <module>
            from setuptools.dist import _get_unpatched
          File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
          File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
          File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/_virtualenv.py", line 89, in exec_module
            old(module)
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_dc5a6011e02d4c70ad915109965f64c5/setuptools/dist.py", line 102
            except ValueError, e:
                             ^
        SyntaxError: invalid syntax
        ----------------------------------------
    WARNING: Discarding https://files.pythonhosted.org/packages/dc/b6/95cf18e73df8fc85ddad57ba3b49ab40104267c26edddc28bb5075b4476f/distribute-0.6.4.tar.gz#sha256=12945da48fb1857c0ef27ba351fa76a1975c11b0d5bc4832895282fcdc4352a2 (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
        ERROR: Command errored out with exit status 1:
         command: '/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_f809b83d6f7a411481118de03a2a3cd7/setup.py'"'"'; __file__='"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_f809b83d6f7a411481118de03a2a3cd7/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-pip-egg-info-7umnt0g2
             cwd: /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_f809b83d6f7a411481118de03a2a3cd7/
        Complete output (15 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_f809b83d6f7a411481118de03a2a3cd7/setuptools/__init__.py", line 2, in <module>
            from setuptools.extension import Extension, Library
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_f809b83d6f7a411481118de03a2a3cd7/setuptools/extension.py", line 2, in <module>
            from setuptools.dist import _get_unpatched
          File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
          File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
          File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/_virtualenv.py", line 89, in exec_module
            old(module)
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_f809b83d6f7a411481118de03a2a3cd7/setuptools/dist.py", line 102
            except ValueError, e:
                             ^
        SyntaxError: invalid syntax
        ----------------------------------------
    WARNING: Discarding https://files.pythonhosted.org/packages/ac/c2/d271d54e5dd82d5727cac67bfe0b84ce508120082073a989943740008394/distribute-0.6.3.zip#sha256=a121a30700cd2f6bb1613f71bd8a44de1fe434ca50f7b316b97d8a5b2b535914 (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
        ERROR: Command errored out with exit status 1:
         command: '/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_c4719630d9504465ac23505feeda8132/setup.py'"'"'; __file__='"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_c4719630d9504465ac23505feeda8132/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-pip-egg-info-rbxar2_u
             cwd: /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_c4719630d9504465ac23505feeda8132/
        Complete output (15 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_c4719630d9504465ac23505feeda8132/setuptools/__init__.py", line 2, in <module>
            from setuptools.extension import Extension, Library
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_c4719630d9504465ac23505feeda8132/setuptools/extension.py", line 2, in <module>
            from setuptools.dist import _get_unpatched
          File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
          File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
          File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/_virtualenv.py", line 89, in exec_module
            old(module)
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_c4719630d9504465ac23505feeda8132/setuptools/dist.py", line 102
            except ValueError, e:
                             ^
        SyntaxError: invalid syntax
        ----------------------------------------
    WARNING: Discarding https://files.pythonhosted.org/packages/81/a2/b6371ad2b865656293ad9d064b0bca6c32283a9acc35ec455b05d820da0f/distribute-0.6.3.tar.gz#sha256=dc097ed5f75ed141cfe27c2c9718447b39c2c1d659bcca041302efb6384d4c41 (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
        ERROR: Command errored out with exit status 1:
         command: '/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_ac08e4d021344afca90f6263ab8f218c/setup.py'"'"'; __file__='"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_ac08e4d021344afca90f6263ab8f218c/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-pip-egg-info-u900avr0
             cwd: /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_ac08e4d021344afca90f6263ab8f218c/
        Complete output (15 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_ac08e4d021344afca90f6263ab8f218c/setuptools/__init__.py", line 2, in <module>
            from setuptools.extension import Extension, Library
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_ac08e4d021344afca90f6263ab8f218c/setuptools/extension.py", line 2, in <module>
            from setuptools.dist import _get_unpatched
          File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
          File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
          File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/_virtualenv.py", line 89, in exec_module
            old(module)
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_ac08e4d021344afca90f6263ab8f218c/setuptools/dist.py", line 102
            except ValueError, e:
                             ^
        SyntaxError: invalid syntax
        ----------------------------------------
    WARNING: Discarding https://files.pythonhosted.org/packages/88/59/82c73ff573b7ed1b7a831cd51f81cff351fa53514bcd1851e522deb2a9ec/distribute-0.6.2.zip#sha256=5bd8ebc58dea3659ded73f1b8fd070b09e6e22acb1b5745686c743e2782d53ee (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
        ERROR: Command errored out with exit status 1:
         command: '/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_b9448a8b962547959ae1350f1820bebf/setup.py'"'"'; __file__='"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_b9448a8b962547959ae1350f1820bebf/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-pip-egg-info-wi2er5yb
             cwd: /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_b9448a8b962547959ae1350f1820bebf/
        Complete output (15 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_b9448a8b962547959ae1350f1820bebf/setuptools/__init__.py", line 2, in <module>
            from setuptools.extension import Extension, Library
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_b9448a8b962547959ae1350f1820bebf/setuptools/extension.py", line 2, in <module>
            from setuptools.dist import _get_unpatched
          File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
          File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
          File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/_virtualenv.py", line 89, in exec_module
            old(module)
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_b9448a8b962547959ae1350f1820bebf/setuptools/dist.py", line 102
            except ValueError, e:
                             ^
        SyntaxError: invalid syntax
        ----------------------------------------
    WARNING: Discarding https://files.pythonhosted.org/packages/c6/c0/e422bfe70ea4c087a3a4b10d9ca249196394fd7c7bd97d37f1c30e184cbf/distribute-0.6.2.tar.gz#sha256=dd04265d390db326a60de73c24e50468edb7048198d43bb2a5fa74525e35d294 (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
        ERROR: Command errored out with exit status 1:
         command: '/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_1b4dbe09f0d7432287d6d6b112fee0e7/setup.py'"'"'; __file__='"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_1b4dbe09f0d7432287d6d6b112fee0e7/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-pip-egg-info-tzhtu2v3
             cwd: /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_1b4dbe09f0d7432287d6d6b112fee0e7/
        Complete output (15 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_1b4dbe09f0d7432287d6d6b112fee0e7/setuptools/__init__.py", line 2, in <module>
            from setuptools.extension import Extension, Library
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_1b4dbe09f0d7432287d6d6b112fee0e7/setuptools/extension.py", line 2, in <module>
            from setuptools.dist import _get_unpatched
          File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
          File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
          File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/_virtualenv.py", line 89, in exec_module
            old(module)
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_1b4dbe09f0d7432287d6d6b112fee0e7/setuptools/dist.py", line 102
            except ValueError, e:
                             ^
        SyntaxError: invalid syntax
        ----------------------------------------
    WARNING: Discarding https://files.pythonhosted.org/packages/4f/5a/2c01b3bb9fef9e6fc4673925c974f18ff9d3c6a7513208a5513d6dc2298e/distribute-0.6.1.zip#sha256=fe57c7ab40f5a8e0764f0b737a4df08dd3818f123b008e50f7493adbda7426b5 (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
        ERROR: Command errored out with exit status 1:
         command: '/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_1f363cab876c4419935c2992531a266a/setup.py'"'"'; __file__='"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_1f363cab876c4419935c2992531a266a/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-pip-egg-info-gjrp5yzk
             cwd: /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_1f363cab876c4419935c2992531a266a/
        Complete output (15 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_1f363cab876c4419935c2992531a266a/setuptools/__init__.py", line 2, in <module>
            from setuptools.extension import Extension, Library
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_1f363cab876c4419935c2992531a266a/setuptools/extension.py", line 2, in <module>
            from setuptools.dist import _get_unpatched
          File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
          File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
          File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/_virtualenv.py", line 89, in exec_module
            old(module)
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_1f363cab876c4419935c2992531a266a/setuptools/dist.py", line 102
            except ValueError, e:
                             ^
        SyntaxError: invalid syntax
        ----------------------------------------
    WARNING: Discarding https://files.pythonhosted.org/packages/42/2f/77365178cb4567987d0248f05d7c5adfad2b04bacfbfbc9bc6320b2575dc/distribute-0.6.1.tar.gz#sha256=4e2d26047c7ca7cea83d178de04ca44c40e137f412252ac59878759e37fc60ff (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
        ERROR: Command errored out with exit status 1:
         command: '/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_72f340d3fed947a48d580082524ef24d/setup.py'"'"'; __file__='"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_72f340d3fed947a48d580082524ef24d/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-pip-egg-info-anscw9i7
             cwd: /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_72f340d3fed947a48d580082524ef24d/
        Complete output (15 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_72f340d3fed947a48d580082524ef24d/setuptools/__init__.py", line 2, in <module>
            from setuptools.extension import Extension, Library
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_72f340d3fed947a48d580082524ef24d/setuptools/extension.py", line 2, in <module>
            from setuptools.dist import _get_unpatched
          File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
          File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
          File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/_virtualenv.py", line 89, in exec_module
            old(module)
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_72f340d3fed947a48d580082524ef24d/setuptools/dist.py", line 102
            except ValueError, e:
                             ^
        SyntaxError: invalid syntax
        ----------------------------------------
    WARNING: Discarding https://files.pythonhosted.org/packages/f5/a1/5d176b200da15f6a1cbd50115d7218ddcbd8764c4ea300768b37ca123a69/distribute-0.6.zip#sha256=2f3f6c44d398c91238658cf831773b9f8b0927c4eef694879b95b0e784e588df (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
        ERROR: Command errored out with exit status 1:
         command: '/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_8fb48e6d16244d7f9c318023f4e8e90a/setup.py'"'"'; __file__='"'"'/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_8fb48e6d16244d7f9c318023f4e8e90a/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-pip-egg-info-mff5p9ac
             cwd: /private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_8fb48e6d16244d7f9c318023f4e8e90a/
        Complete output (15 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_8fb48e6d16244d7f9c318023f4e8e90a/setuptools/__init__.py", line 2, in <module>
            from setuptools.extension import Extension, Library
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_8fb48e6d16244d7f9c318023f4e8e90a/setuptools/extension.py", line 2, in <module>
            from setuptools.dist import _get_unpatched
          File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
          File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
          File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/_virtualenv.py", line 89, in exec_module
            old(module)
          File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-wheel-_ootnfdx/distribute_8fb48e6d16244d7f9c318023f4e8e90a/setuptools/dist.py", line 102
            except ValueError, e:
                             ^
        SyntaxError: invalid syntax
        ----------------------------------------
    WARNING: Discarding https://files.pythonhosted.org/packages/2b/37/8468dd6c136d01adbd031f58b62fc6a8dbd1aedcfbeca2b86f298a960849/distribute-0.6.tar.gz#sha256=0520df7dd20b84233dce5f8c1b284cf88a75621eb7c9b84e0358e77a6ffde68c (from https://pypi.org/simple/distribute/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
    ERROR: Could not find a version that satisfies the requirement distribute
    ERROR: No matching distribution found for distribute
    Traceback (most recent call last):
      File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/setuptools/installer.py", line 75, in fetch_build_egg
        subprocess.check_call(cmd)
      File "/usr/local/Cellar/python@3.9/3.9.4/Frameworks/Python.framework/Versions/3.9/lib/python3.9/subprocess.py", line 373, in check_call
        raise CalledProcessError(retcode, cmd)
    subprocess.CalledProcessError: Command '['/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python', '-m', 'pip', '--disable-pip-version-check', 'wheel', '--no-deps', '-w', '/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/tmp8ac0y2fe', '--quiet', 'distribute']' returned non-zero exit status 1.
    
    The above exception was the direct cause of the following exception:
    
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "/private/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/pip-install-ky8ogv5c/dotenv_3756bd9cff3247d69ac73bf8a820e818/setup.py", line 13, in <module>
        setup(name='dotenv',
      File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/setuptools/__init__.py", line 152, in setup
        _install_setup_requires(attrs)
      File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/setuptools/__init__.py", line 147, in _install_setup_requires
        dist.fetch_build_eggs(dist.setup_requires)
      File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/setuptools/dist.py", line 721, in fetch_build_eggs
        resolved_dists = pkg_resources.working_set.resolve(
      File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/pkg_resources/__init__.py", line 766, in resolve
        dist = best[req.key] = env.best_match(
      File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/pkg_resources/__init__.py", line 1051, in best_match
        return self.obtain(req, installer)
      File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/pkg_resources/__init__.py", line 1063, in obtain
        return installer(requirement)
      File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/setuptools/dist.py", line 780, in fetch_build_egg
        return fetch_build_egg(self, req)
      File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/setuptools/installer.py", line 77, in fetch_build_egg
        raise DistutilsError(str(e)) from e
    distutils.errors.DistutilsError: Command '['/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/bin/python', '-m', 'pip', '--disable-pip-version-check', 'wheel', '--no-deps', '-w', '/var/folders/z9/tmjnhgf92kbgvf4f9jctmyhr0000gn/T/tmp8ac0y2fe', '--quiet', 'distribute']' returned non-zero exit status 1.
    ----------------------------------------