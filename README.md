# autograph-load-test

Hacky scripts to load test the autograph end points for [bug 1471197](https://bugzilla.mozilla.org/show_bug.cgi?id=1471197)

These are set up on signing-linux-dev1, but I wanted to add them here in case something happens to them. The main thing is, we'll need to populate `/builds/scriptworker/aki/` as expected, and create a `/builds/scriptworker/aki/passwords.json` with the autograph configs.

```
/builds/scriptworker/aki:

./script_config.json
./work/task.json
./work/cot/eiQZF2TcT2q8_ILvb2d_tQ/public/build/target.complete.mar
./passwords.json
./artifacts/
./run.sh
```

`passwords.json` looks like [this](https://github.com/escapewindow/build-puppet/blob/autograph-dep/modules/signing_scriptworker/templates/dep-passwords.json.erb).

1. set up the source dir above
2. run `populate.py` in `/builds/scriptworker/load`
3. copy all.sh into `/builds/scriptworker/load`
4. run all.sh
5. spot check `{1..20}/log*`
