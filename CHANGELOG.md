# Changelog

## 0.1.0-alpha.2 (2025-11-04)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/zbdpay/zbd-payments-python-sdk/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

* clean up environment call outs ([535e5ab](https://github.com/zbdpay/zbd-payments-python-sdk/commit/535e5abe6894630fd12397c95e9fdcb0bdfcf658))
* **client:** support file upload requests ([b3a0224](https://github.com/zbdpay/zbd-payments-python-sdk/commit/b3a02242d357e96493899e6acb0f283b83060aef))
* improve future compat with pydantic v3 ([1c2b2a0](https://github.com/zbdpay/zbd-payments-python-sdk/commit/1c2b2a067518c006ed2ea1d5e3f3c28f2868b55e))
* **types:** replace List[str] with SequenceNotStr in params ([3a6e9d2](https://github.com/zbdpay/zbd-payments-python-sdk/commit/3a6e9d20ae545ee635cd86b7ae4b7b1f4705763f))


### Bug Fixes

* avoid newer type syntax ([5b84026](https://github.com/zbdpay/zbd-payments-python-sdk/commit/5b840269faac165f86335e1177eccbc3d47651c0))
* **client:** close streams without requiring full consumption ([5f08b58](https://github.com/zbdpay/zbd-payments-python-sdk/commit/5f08b58994542a3fb4b2f9a4a766f545b1c8d809))
* **client:** don't send Content-Type header on GET requests ([288eb7d](https://github.com/zbdpay/zbd-payments-python-sdk/commit/288eb7dbc10084e010006e07a0b6ae8bc31830f8))
* **parsing:** correctly handle nested discriminated unions ([2ba6e54](https://github.com/zbdpay/zbd-payments-python-sdk/commit/2ba6e54f3688d3606a32b54e67858a9c1121ed03))
* **parsing:** ignore empty metadata ([6810653](https://github.com/zbdpay/zbd-payments-python-sdk/commit/6810653d722e8eb4b5531d1a120035001942e039))
* **parsing:** parse extra field types ([f952799](https://github.com/zbdpay/zbd-payments-python-sdk/commit/f9527997050c628fee3f05b76420e1449238d13b))


### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([127bafc](https://github.com/zbdpay/zbd-payments-python-sdk/commit/127bafcd8d74f9dffa1c574b9b3cccc92e7f18ef))
* **ci:** change upload type ([9c44657](https://github.com/zbdpay/zbd-payments-python-sdk/commit/9c4465773de134e1ecacb494a4f3f3c5f174146b))
* do not install brew dependencies in ./scripts/bootstrap by default ([fea8954](https://github.com/zbdpay/zbd-payments-python-sdk/commit/fea89541e9d5e4373720e0639d09d574b6b681be))
* **internal/tests:** avoid race condition with implicit client cleanup ([81b1d27](https://github.com/zbdpay/zbd-payments-python-sdk/commit/81b1d27d18635a5ee76009d44be19da36b3ccaf8))
* **internal:** add Sequence related utils ([9159c6d](https://github.com/zbdpay/zbd-payments-python-sdk/commit/9159c6d5474db3fb12ec5597b817c17c4151230a))
* **internal:** bump pinned h11 dep ([3938712](https://github.com/zbdpay/zbd-payments-python-sdk/commit/3938712b4835065e531e220a3e277bd84c0a6cf8))
* **internal:** change ci workflow machines ([94573cf](https://github.com/zbdpay/zbd-payments-python-sdk/commit/94573cffbdaaa47ea3c04c8c08594ef8bcf515a9))
* **internal:** codegen related update ([b0af041](https://github.com/zbdpay/zbd-payments-python-sdk/commit/b0af041c74a92ea2be802ba5470c1f76a6b6c22d))
* **internal:** codegen related update ([281314a](https://github.com/zbdpay/zbd-payments-python-sdk/commit/281314a9a7b24c8e61947df03ec796e162475447))
* **internal:** codegen related update ([f6b6595](https://github.com/zbdpay/zbd-payments-python-sdk/commit/f6b6595872a031ad6fa6dd2b48f3ed7259fcdd55))
* **internal:** detect missing future annotations with ruff ([8c6c43a](https://github.com/zbdpay/zbd-payments-python-sdk/commit/8c6c43a7f9ecb965948a2c0c4e45ede5929e3f2d))
* **internal:** fix ruff target version ([bfb7eb6](https://github.com/zbdpay/zbd-payments-python-sdk/commit/bfb7eb6f5f90f2eef5be4714c25d2335cd340956))
* **internal:** grammar fix (it's -&gt; its) ([5aa138a](https://github.com/zbdpay/zbd-payments-python-sdk/commit/5aa138a2baca8ff95452be8dd90cb916d909a09d))
* **internal:** update comment in script ([da3e700](https://github.com/zbdpay/zbd-payments-python-sdk/commit/da3e7007adac9551b21b7525c895538b0072e3de))
* **internal:** update pydantic dependency ([6febfc0](https://github.com/zbdpay/zbd-payments-python-sdk/commit/6febfc07161f1678bd35a446b2fd618a7c08fc8d))
* **internal:** update pyright exclude list ([e087e8a](https://github.com/zbdpay/zbd-payments-python-sdk/commit/e087e8abacb81f209f9a9746ee4f5e666d21d36d))
* **package:** mark python 3.13 as supported ([ca53a0e](https://github.com/zbdpay/zbd-payments-python-sdk/commit/ca53a0eaa744e881b8d24a05f2d35049a9815682))
* **project:** add settings file for vscode ([36c1d48](https://github.com/zbdpay/zbd-payments-python-sdk/commit/36c1d48714b6c9750dd885ee93c5e041f4a6e59e))
* **readme:** fix version rendering on pypi ([337d17e](https://github.com/zbdpay/zbd-payments-python-sdk/commit/337d17e1d4ad645f55793d615ebd9f328fdef08a))
* **tests:** simplify `get_platform` test ([c354e32](https://github.com/zbdpay/zbd-payments-python-sdk/commit/c354e32d12201983196cde30acd370ee6e6c0941))
* **types:** change optional parameter type from NotGiven to Omit ([037353e](https://github.com/zbdpay/zbd-payments-python-sdk/commit/037353e3016446a51197a1dafdb9f50ca4156804))
* update @stainless-api/prism-cli to v5.15.0 ([f365ac1](https://github.com/zbdpay/zbd-payments-python-sdk/commit/f365ac1076dab4f1f57bb95878560a7eb94731a1))
* update github action ([cc78ddf](https://github.com/zbdpay/zbd-payments-python-sdk/commit/cc78ddff5b244d94a49e6558dfe665d156791c58))

## 0.1.0-alpha.1 (2025-06-30)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/zbdpay/zbd-payments-python-sdk/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** update via SDK Studio ([e140140](https://github.com/zbdpay/zbd-payments-python-sdk/commit/e1401402adc0922f9d480bd4915508829a012ea6))
* **api:** update via SDK Studio ([d365689](https://github.com/zbdpay/zbd-payments-python-sdk/commit/d365689aea13350770ebb29003703506b2d93bc6))
* **api:** update via SDK Studio ([77175a0](https://github.com/zbdpay/zbd-payments-python-sdk/commit/77175a07ea0bd1874d86fecb7b82e2e2388bacb0))
* **client:** add support for aiohttp ([8788187](https://github.com/zbdpay/zbd-payments-python-sdk/commit/8788187346d655321d0f7039833533060ad23a58))


### Bug Fixes

* **ci:** correct conditional ([80e453a](https://github.com/zbdpay/zbd-payments-python-sdk/commit/80e453a6e788e1d0486512289db060a0c2116c4b))
* **ci:** release-doctor — report correct token name ([80668d2](https://github.com/zbdpay/zbd-payments-python-sdk/commit/80668d2c8e761c84183950b40f2d01319f0cbbe3))


### Chores

* change publish docs url ([ade5ab6](https://github.com/zbdpay/zbd-payments-python-sdk/commit/ade5ab6d9c14e7f91a6cbb1addf75189ae3dc42e))
* **ci:** only run for pushes and fork pull requests ([859534a](https://github.com/zbdpay/zbd-payments-python-sdk/commit/859534a6d07900299587933720f1054d5b67d036))
* configure new SDK language ([679c119](https://github.com/zbdpay/zbd-payments-python-sdk/commit/679c119fa94c1e1c88d78576c52b183be1dca2ca))
* configure new SDK language ([07173a5](https://github.com/zbdpay/zbd-payments-python-sdk/commit/07173a50fe45ea94e40ed83b04dc09384bf458e1))
* **internal:** codegen related update ([5cba4a2](https://github.com/zbdpay/zbd-payments-python-sdk/commit/5cba4a2c05d6d3a8a483ada0c22720aaeb619303))
* **tests:** skip some failing tests on the latest python versions ([680eed5](https://github.com/zbdpay/zbd-payments-python-sdk/commit/680eed5b78810d2296df2e60a3c8bf0f11c73d51))
* update SDK settings ([9be94bf](https://github.com/zbdpay/zbd-payments-python-sdk/commit/9be94bf044c25787f3832724f9f00ad05e0d5878))
