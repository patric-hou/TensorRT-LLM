# TensorRT-LLM PR详细分析总表（改进版）

本表基于**改进的CI失败检测逻辑**重新分析了所有441个PR。

## 改进要点

### ✅ 改进的CI失败检测标准

1. **只统计CI机器人的评论**
   - tensorrt-cicd ✅
   - blossomci ✅
   - github-actions[bot] ✅
   - CodeRabbitAI ❌ (静态检查，不是CI)

2. **必须包含明确的失败状态**
   - `status: 'FAILURE'` ✅
   - `state 'FAILURE'` ✅
   - `completed with status: FAILED` ✅

3. **排除误判情况**
   - "/bot skip --comment 'waive failed'" ❌ (Bot命令)
   - "Fix failed test" ❌ (讨论)
   - "Failed checks (warning)" ❌ (CodeRabbit静态检查)

4. **综合判断**
   - 如果同一评论既有FAILURE又有SUCCESS，以最后出现的为准

### 📊 阻塞类型

| 类型 | 是否计入阻塞 | 说明 |
|------|------------|------|
| CI检查失败 | ✅ 是 | 真实的CI/CD流水线失败 |
| Review Changes Requested | ✅ 是 | 审查者要求修改代码 |
| PR标题格式 | ⚠️ 否 | 仅警告，可直接修改 |

---

## PR详细列表

| PR | 标题 | 阻塞次数 | 阻塞详情 | Commit数 | Commits列表 |
|---|---|---|---|---|---|
| [#10870](https://github.com/NVIDIA/TensorRT-LLM/pull/10870) | [None][chore] Revert NVIDIA/TensorRT-LLM#10819 | 0 | - | 2 | 2次提交 |
| [#10847](https://github.com/NVIDIA/TensorRT-LLM/pull/10847) | [None][chore] Reduce tedious logs | 0 | - | 1 | [`12a1796`](https://github.com/NVIDIA/TensorRT-LLM/commit/12a17964b08ff6d6bc4ebb90daf7fdcbead38afd) |
| [#10822](https://github.com/NVIDIA/TensorRT-LLM/pull/10822) | [None][fix] Fix the potential access issue of cache operations between ranks. | 0 | - | 1 | 1次提交 |
| [#10795](https://github.com/NVIDIA/TensorRT-LLM/pull/10795) | [None][infra] Waive failed case for release branch on 01/19 | 0 | - | 1 | 1次提交 |
| [#10793](https://github.com/NVIDIA/TensorRT-LLM/pull/10793) | [https://nvbugs/5814253][fix] unwaive test_autotuner_distributed_strategy tests | 4 | • CI检查失败 (4次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/10793#issuecomment-) | 2 | [`d94343d`](https://github.com/NVIDIA/TensorRT-LLM/commit/d94343d827043ba5aba9b3381e541c53b78bfd6c), [`c7034ee`](https://github.com/NVIDIA/TensorRT-LLM/commit/c7034ee8689efbdb3f3fba8d33d9e42e5c8c0314) |
| [#10792](https://github.com/NVIDIA/TensorRT-LLM/pull/10792) | [None][chore] switch to ConfigurableMoE as the default path | 5 | • CI检查失败 (5次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/10792#issuecomment-) | 1 | 1次提交 |
| [#10779](https://github.com/NVIDIA/TensorRT-LLM/pull/10779) | [None][test] modify ctx config in 128k8k disagg cases | 0 | - | 3 | 3次提交 |
| [#10746](https://github.com/NVIDIA/TensorRT-LLM/pull/10746) | [None][doc] update doc (add minimax model) | 0 | - | 1 | 1次提交 |
| [#10727](https://github.com/NVIDIA/TensorRT-LLM/pull/10727) | [None][fix] AutoDeploy: Fix the nvfp4 fused_moe | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/10727#issuecomment-) | 6 | 6次提交 |
| [#10691](https://github.com/NVIDIA/TensorRT-LLM/pull/10691) | [TRTLLM-9111][feat] MoE test refactor: Extend MoE quantization test utilities wi | 0 | - | 1 | 1次提交 |
| [#10670](https://github.com/NVIDIA/TensorRT-LLM/pull/10670) | [None][fix] fix L0 issues | 0 | - | 1 | [`c40e0e2`](https://github.com/NVIDIA/TensorRT-LLM/commit/c40e0e23ee24a669edfc677708b473a35f17113a) |
| [#10660](https://github.com/NVIDIA/TensorRT-LLM/pull/10660) | [https://nvbugs/5794313][chore] unwaive tests. | 7 | • CI检查失败 (7次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/10660#issuecomment-) | 5 | [`6189380`](https://github.com/NVIDIA/TensorRT-LLM/commit/61893809ab38362d52512b902eacf501ab041d48), [`d5ed7d7`](https://github.com/NVIDIA/TensorRT-LLM/commit/d5ed7d78623e32d96b51b638a99873a19e1ec263), [`d8b63fc`](https://github.com/NVIDIA/TensorRT-LLM/commit/d8b63fc457c15edfb313c54d4e21e439538489a4), [`0ad3f5d`](https://github.com/NVIDIA/TensorRT-LLM/commit/0ad3f5d547397ddfd4df435967727d8a633a3149), [`447713d`](https://github.com/NVIDIA/TensorRT-LLM/commit/447713dcedd41f6910505294dc6e34e956d0e61e) |
| [#10629](https://github.com/NVIDIA/TensorRT-LLM/pull/10629) | [None][test] add log_samples and output_path for trtllm_eval | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/10629#issuecomment-) | 2 | [`3f9421a`](https://github.com/NVIDIA/TensorRT-LLM/commit/3f9421ac3da258baf8b4b391449140bc561d9c95), [`b3d0f4a`](https://github.com/NVIDIA/TensorRT-LLM/commit/b3d0f4a883c038f0573d7844db40009c6ef7c5bd) |
| [#10597](https://github.com/NVIDIA/TensorRT-LLM/pull/10597) | [None][chore] Print correct backend name in benchmark report | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/10597#issuecomment-) | 1 | 1次提交 |
| [#10561](https://github.com/NVIDIA/TensorRT-LLM/pull/10561) | [None][feat] Add support for DeepSeek v3.2 tests | 0 | - | 8 | [`62398b2`](https://github.com/NVIDIA/TensorRT-LLM/commit/62398b29ddde2a7f871104e796ca4a0b4f35041a), [`663b45c`](https://github.com/NVIDIA/TensorRT-LLM/commit/663b45c7ef7b9cfcd8e03d01dbcdc03fe5401d5f), [`750bc69`](https://github.com/NVIDIA/TensorRT-LLM/commit/750bc6967a51ed2b189d0c0fc3b0a7ea1ea36eeb), [`5bbaf56`](https://github.com/NVIDIA/TensorRT-LLM/commit/5bbaf5684139a2c6a6e7d00d4b48adae2161b1b1), [`9eb8111`](https://github.com/NVIDIA/TensorRT-LLM/commit/9eb811138a2113f09a67916395a3b3b80fd724c0), [`c395709`](https://github.com/NVIDIA/TensorRT-LLM/commit/c395709103fff747588c0b9ae42c166d9b57eb4c), [`9fe031c`](https://github.com/NVIDIA/TensorRT-LLM/commit/9fe031cc170d3846613cbcf85fdab2f9c6bd6b9e), [`3d21c83`](https://github.com/NVIDIA/TensorRT-LLM/commit/3d21c8342bad870e99b2e13cde62131ddcf00275) |
| [#10516](https://github.com/NVIDIA/TensorRT-LLM/pull/10516) | [https://nvbugs/5628848][fix] Fix nanobind stub generation | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/10516#issuecomment-) | 3 | [`f0589db`](https://github.com/NVIDIA/TensorRT-LLM/commit/f0589db46dcb012776d97de8420c5a95d98244e0), [`26d2e16`](https://github.com/NVIDIA/TensorRT-LLM/commit/26d2e168964be950c8a07f3dea0a3ec70f4b22c0), [`631850e`](https://github.com/NVIDIA/TensorRT-LLM/commit/631850ec6cd4be6afe4a96a61caf7b41ab82bb45) |
| [#10500](https://github.com/NVIDIA/TensorRT-LLM/pull/10500) | [None] [feat] Support multiple accuracy tasks for slurm scripts | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/10500#issuecomment-) | 6 | 6次提交 |
| [#10499](https://github.com/NVIDIA/TensorRT-LLM/pull/10499) | [https://nvbugs/5788127][fix] Use uint64_t as the dtype of lamport_buffer_size t | 7 | • CI检查失败 (7次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/10499#issuecomment-) | 1 | 1次提交 |
| [#10489](https://github.com/NVIDIA/TensorRT-LLM/pull/10489) | [TRTLLM-10248][feat] Support Bot to Send Perf Regression Msg to Slack Channel | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/10489#issuecomment-) | 1 | [`831e588`](https://github.com/NVIDIA/TensorRT-LLM/commit/831e588e4d393de4f9098117a321b40ab38bd376) |
| [#10466](https://github.com/NVIDIA/TensorRT-LLM/pull/10466) | [https://nvbugs/5732942][fix] AutoDeploy: handle transformers 4.57.1 upgrade fix | 0 | - | 1 | 1次提交 |
| [#10452](https://github.com/NVIDIA/TensorRT-LLM/pull/10452) | [None][chore] remove redundant retries while binding to arbitrary port | 0 | - | 1 | 1次提交 |
| [#10451](https://github.com/NVIDIA/TensorRT-LLM/pull/10451) | [https://nvbugs/5753788][chore] Padding empty chunk for configurable moe | 7 | • CI检查失败 (7次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/10451#issuecomment-) | 3 | 3次提交 |
| [#10444](https://github.com/NVIDIA/TensorRT-LLM/pull/10444) | [https://nvbugs/5701445][chore] isolate test. | 8 | • CI检查失败 (8次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/10444#issuecomment-) | 6 | 6次提交 |
| [#10442](https://github.com/NVIDIA/TensorRT-LLM/pull/10442) | [None][test] restrict max_num_tokens in disagg mtp config | 0 | - | 3 | 3次提交 |
| [#10429](https://github.com/NVIDIA/TensorRT-LLM/pull/10429) | [None] [feat] Add test script and raster M for gather fc1 kernel | 0 | - | 4 | [`ad654b8`](https://github.com/NVIDIA/TensorRT-LLM/commit/ad654b8fc86f6ec13c823bc5313ab6686a9f2c06), [`40f4411`](https://github.com/NVIDIA/TensorRT-LLM/commit/40f441141a0425a788bb15e773ea85d6ec10b713), [`8c3aa4e`](https://github.com/NVIDIA/TensorRT-LLM/commit/8c3aa4e05e9f75149900997b622e2fed6a1132ac), [`e129576`](https://github.com/NVIDIA/TensorRT-LLM/commit/e129576d8e817bdc26d2c80ba685bbd5063783b1) |
| [#10386](https://github.com/NVIDIA/TensorRT-LLM/pull/10386) | [https://nvbugs/5772521][fix] Fix draft token tree chain crash | 0 | - | 1 | [`927e975`](https://github.com/NVIDIA/TensorRT-LLM/commit/927e975ec83f0a4259ad67ea885f081732dbe93d) |
| [#10341](https://github.com/NVIDIA/TensorRT-LLM/pull/10341) | [https://nvbugs/5769890][fix] Import get_free_port. | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/10341#issuecomment-) | 1 | [`bfe0940`](https://github.com/NVIDIA/TensorRT-LLM/commit/bfe0940963f195dd74ddb8697d0190b3f14027ca) |
| [#10336](https://github.com/NVIDIA/TensorRT-LLM/pull/10336) | [TRTLLM-10185][feat] AutoTuner Cache: Support cache file lock and merge all rank | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/10336#issuecomment-) | 1 | 1次提交 |
| [#10301](https://github.com/NVIDIA/TensorRT-LLM/pull/10301) | [None][chore] Add failed cases into waives.txt | 0 | - | 4 | 4次提交 |
| [#10293](https://github.com/NVIDIA/TensorRT-LLM/pull/10293) | [None][ci] Waive TestLlama3_1_8B::test_auto_dtype[False-2] for timeout | 0 | - | 1 | [`308f8fb`](https://github.com/NVIDIA/TensorRT-LLM/commit/308f8fbe1439a12a41f73ff68441abdf2270d4c1) |
| [#10284](https://github.com/NVIDIA/TensorRT-LLM/pull/10284) | [None][feat] Speculative One Model: FlashInfer sampling | 6 | • CI检查失败 (6次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/10284#issuecomment-) | 1 | 1次提交 |
| [#10271](https://github.com/NVIDIA/TensorRT-LLM/pull/10271) | [https://nvbugs/5766986][fix] fixed the shard_all_unprocessed default value to a | 4 | • CI检查失败 (4次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/10271#issuecomment-) | 2 | 2次提交 |
| [#10256](https://github.com/NVIDIA/TensorRT-LLM/pull/10256) | [None][feat] Drop non-deepgemm fp8 block scale gemm | 3 | • CI检查失败 (3次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/10256#issuecomment-) | 1 | [`5af7f45`](https://github.com/NVIDIA/TensorRT-LLM/commit/5af7f452be68afe419a4c7db8c041b53b4bf7e4c) |
| [#10215](https://github.com/NVIDIA/TensorRT-LLM/pull/10215) | [https://nvbugs/5622938][feat] Run sample_async on extra stream. | 4 | • CI检查失败 (4次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/10215#issuecomment-) | 7 | 7次提交 |
| [#10197](https://github.com/NVIDIA/TensorRT-LLM/pull/10197) | [None][fix] Fix the bug for top_k=10 in NVLinkOneSided AlltoAll. | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/10197#issuecomment-) | 1 | 1次提交 |
| [#10194](https://github.com/NVIDIA/TensorRT-LLM/pull/10194) | [https://nvbugs/5762016][chore] Skip a ray test | 0 | - | 1 | 1次提交 |
| [#10135](https://github.com/NVIDIA/TensorRT-LLM/pull/10135) | [https://nvbugs/5747911][fix] Use offline data path for the unit test of mmencod | 0 | - | 2 | [`2ede206`](https://github.com/NVIDIA/TensorRT-LLM/commit/2ede206d15043969389dfe222128ed0cc9be6599), [`7015459`](https://github.com/NVIDIA/TensorRT-LLM/commit/7015459be2f36eca7999760bcaf7fc2eb59f96e4) |
| [#10125](https://github.com/NVIDIA/TensorRT-LLM/pull/10125) | [TRTC-121] [feat] Add recipe selector UI to complement the recipe database | 3 | • CI检查失败 (3次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/10125#issuecomment-) | 13 | 13次提交 |
| [#10097](https://github.com/NVIDIA/TensorRT-LLM/pull/10097) | [None][infra] Update allowlist 2025.12.17 | 0 | - | 1 | 1次提交 |
| [#10082](https://github.com/NVIDIA/TensorRT-LLM/pull/10082) | [TRTLLM-9455][feat] support for new checkpoint | 5 | • CI检查失败 (5次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/10082#issuecomment-) | 4 | 4次提交 |
| [#10062](https://github.com/NVIDIA/TensorRT-LLM/pull/10062) | [https://nvbugs/5729697][fix] MNNVL Allreduce: use CUDA runtime instead of Macro | 5 | • CI检查失败 (5次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/10062#issuecomment-) | 4 | 4次提交 |
| [#10060](https://github.com/NVIDIA/TensorRT-LLM/pull/10060) | [https://nvbugs/5717993][fix] Add execution_stream across PyExecutor, KVCacheMan | 4 | • CI检查失败 (4次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/10060#issuecomment-) | 6 | 6次提交 |
| [#10055](https://github.com/NVIDIA/TensorRT-LLM/pull/10055) | [None][infra] Move install_boost from install_triton.sh to install_base.sh | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/10055#issuecomment-) | 3 | 3次提交 |
| [#10043](https://github.com/NVIDIA/TensorRT-LLM/pull/10043) | [TRTLLM-9992][perf] Enable PDL for CuteDSL kernels and overlap MoeOutputMemset | 5 | • CI检查失败 (5次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/10043#issuecomment-) | 9 | 9次提交 |
| [#10040](https://github.com/NVIDIA/TensorRT-LLM/pull/10040) | [TRTLLM-9989][fix] Disable tvm_ffi for CuteDSL nvFP4 dense GEMM. | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/10040#issuecomment-) | 4 | 4次提交 |
| [#10005](https://github.com/NVIDIA/TensorRT-LLM/pull/10005) | [TRTC-102][docs] `--extra_llm_api_options`->`--config` in docs/examples/tests | 6 | • CI检查失败 (6次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/10005#issuecomment-) | 11 | 11次提交 |
| [#9996](https://github.com/NVIDIA/TensorRT-LLM/pull/9996) | [None][infra] Add multi gpu Ray tests into L0 merge change request list. | 0 | - | 2 | 2次提交 |
| [#9986](https://github.com/NVIDIA/TensorRT-LLM/pull/9986) | [TRTLLM-9493][feat] Custom AllToAll for helix parallelism | 6 | • CI检查失败 (6次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/9986#issuecomment-) | 3 | 3次提交 |
| [#9984](https://github.com/NVIDIA/TensorRT-LLM/pull/9984) | [TRTLLM-9565][fix] Fix deepseek sharding | 8 | • CI检查失败 (8次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/9984#issuecomment-) | 11 | 11次提交 |
| [#9972](https://github.com/NVIDIA/TensorRT-LLM/pull/9972) | [None][doc] update readme for rpc | 0 | - | 1 | 1次提交 |
| [#9910](https://github.com/NVIDIA/TensorRT-LLM/pull/9910) | [#9717][chore] Refactor MoE code to use enums | 7 | • CI检查失败 (7次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/9910#issuecomment-) | 9 | 9次提交 |
| [#9896](https://github.com/NVIDIA/TensorRT-LLM/pull/9896) | [https://nvbugs/5727481][ci] Fix Port Conflict in Perf-Sanity CI Test | 0 | - | 2 | 2次提交 |
| [#9887](https://github.com/NVIDIA/TensorRT-LLM/pull/9887) | [None][doc] remove nano-vl-v2 model support in release notes | 0 | - | 1 | 1次提交 |
| [#9885](https://github.com/NVIDIA/TensorRT-LLM/pull/9885) | [None][feat] Implement sampling on 1-model EAGLE3 | 3 | • CI检查失败 (3次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/9885#issuecomment-) | 2 | [`1c72ac7`](https://github.com/NVIDIA/TensorRT-LLM/commit/1c72ac7934cc4c9ddde5c266685e99150dbf3746), [`434df69`](https://github.com/NVIDIA/TensorRT-LLM/commit/434df69a16ff621ffd4d8e330be31da2fca61d37) |
| [#9876](https://github.com/NVIDIA/TensorRT-LLM/pull/9876) | [None][ci] Move remaining DGX-B200 tests to LBD | 6 | • CI检查失败 (6次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/9876#issuecomment-) | 3 | 3次提交 |
| [#9853](https://github.com/NVIDIA/TensorRT-LLM/pull/9853) | [TRTINFRA-7328][infra] - Move half B200 tests to lbd | 0 | - | 3 | 3次提交 |
| [#9849](https://github.com/NVIDIA/TensorRT-LLM/pull/9849) | [None][doc] Adding parallelism types in feature combination matrix | 0 | - | 6 | 6次提交 |
| [#9836](https://github.com/NVIDIA/TensorRT-LLM/pull/9836) | [#9640][feat] Migrate model registry to v2.0 format with composable configs | 0 | - | 7 | 7次提交 |
| [#9833](https://github.com/NVIDIA/TensorRT-LLM/pull/9833) | [TRTLLM-9262][test] add groupgemm ada case for rcca | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/9833#issuecomment-) | 1 | 1次提交 |
| [#9812](https://github.com/NVIDIA/TensorRT-LLM/pull/9812) | [https://nvbugs/5597647][ci] Unwaive fixed tests. | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/9812#issuecomment-) | 1 | 1次提交 |
| [#9769](https://github.com/NVIDIA/TensorRT-LLM/pull/9769) | [None][infra] Waive failed cases for main branch on 12/07 | 0 | - | 2 | [`d73a0ad`](https://github.com/NVIDIA/TensorRT-LLM/commit/d73a0ad3b184178c56238f7947cd25eab825ede7), [`1470fcb`](https://github.com/NVIDIA/TensorRT-LLM/commit/1470fcba4c8509d64e2c21528be3d9aafef9b5de) |
| [#9739](https://github.com/NVIDIA/TensorRT-LLM/pull/9739) | [None][doc] Update release notes | 2 | • Review Changes Requested (2次) - [Reviews](https://github.com/NVIDIA/TensorRT-LLM/pull/9739/files) | 8 | 8次提交 |
| [#9649](https://github.com/NVIDIA/TensorRT-LLM/pull/9649) | [None][fix] Fix triton moe load_weight | 3 | • CI检查失败 (3次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/9649#issuecomment-) | 1 | 1次提交 |
| [#9637](https://github.com/NVIDIA/TensorRT-LLM/pull/9637) | [https://nvbugs/5705197][chore] Unwaive timeout disagg tests | 0 | - | 3 | 3次提交 |
| [#9622](https://github.com/NVIDIA/TensorRT-LLM/pull/9622) | [https://nvbugs/5561153][test] Fix log error for perf test | 0 | - | 5 | [`7979353`](https://github.com/NVIDIA/TensorRT-LLM/commit/7979353e5414d91bd82ab11d123929cfd3f38d79), [`f1e78a8`](https://github.com/NVIDIA/TensorRT-LLM/commit/f1e78a8ddb1647ae079ae1fc48d86e2d5b46d61b), [`e7fed55`](https://github.com/NVIDIA/TensorRT-LLM/commit/e7fed5516241439abc6bf1815d324d0bb81c81a3), [`8ac761b`](https://github.com/NVIDIA/TensorRT-LLM/commit/8ac761bda81031967d32152cbd96a4589c1d781b), [`ab5ed41`](https://github.com/NVIDIA/TensorRT-LLM/commit/ab5ed417104d9ce9b59bddcc8b1bc7586101a599) |
| [#9620](https://github.com/NVIDIA/TensorRT-LLM/pull/9620) | [None][infra] Remove an invalid test name in waives.txt | 0 | - | 2 | 2次提交 |
| [#9610](https://github.com/NVIDIA/TensorRT-LLM/pull/9610) | [#9432][fix] Resolve NameError in memory profiler for v0.12.0-jetson branch. | 0 | - | 1 | [`29fd759`](https://github.com/NVIDIA/TensorRT-LLM/commit/29fd7594800c9da303f592ecdf6cbe8ddfc58973) |
| [#9569](https://github.com/NVIDIA/TensorRT-LLM/pull/9569) | [None][fix] Replace hash method with unique_id for cutedsl MoE runners. | 0 | - | 1 | 1次提交 |
| [#9559](https://github.com/NVIDIA/TensorRT-LLM/pull/9559) | [None][ci] Split H100_PCIe-PyTorch-Post-Merge test stage | 0 | - | 1 | 1次提交 |
| [#9544](https://github.com/NVIDIA/TensorRT-LLM/pull/9544) | [None][feat] add chat template kwargs support to longbench-v2 | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/9544#issuecomment-) | 4 | 4次提交 |
| [#9539](https://github.com/NVIDIA/TensorRT-LLM/pull/9539) | [None][infra] Waive failed cases for main branch on 11/28 | 0 | - | 1 | 1次提交 |
| [#9534](https://github.com/NVIDIA/TensorRT-LLM/pull/9534) | [None][chore] remove qwen3-next accuracy tests | 4 | • CI检查失败 (4次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/9534#issuecomment-) | 2 | 2次提交 |
| [#9507](https://github.com/NVIDIA/TensorRT-LLM/pull/9507) | [None][infra] Waive failed case in pre-merge on 11/27 | 0 | - | 1 | 1次提交 |
| [#9506](https://github.com/NVIDIA/TensorRT-LLM/pull/9506) | [https://nvbugs/5422621][test] Add GB 200 WIDEEP test case for RCCA 5422621 | 3 | • CI检查失败 (3次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/9506#issuecomment-) | 20 | 20次提交 |
| [#9491](https://github.com/NVIDIA/TensorRT-LLM/pull/9491) | [None][fix] Correct virtual memory allocation alignment | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/9491#issuecomment-) | 1 | 1次提交 |
| [#9479](https://github.com/NVIDIA/TensorRT-LLM/pull/9479) | [None][fix] change allreduce workspace dtype to torch.int64 to avoid overflow | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/9479#issuecomment-) | 1 | 1次提交 |
| [#9435](https://github.com/NVIDIA/TensorRT-LLM/pull/9435) | [https://nvbugs/5685015][fix] Update invalid max_token test | 0 | - | 1 | 1次提交 |
| [#9375](https://github.com/NVIDIA/TensorRT-LLM/pull/9375) | [None][ci] waive two ray tests | 0 | - | 1 | 1次提交 |
| [#9348](https://github.com/NVIDIA/TensorRT-LLM/pull/9348) | [TRTLLM-7963][fix] Several improvements of autotuning quality | 3 | • CI检查失败 (3次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/9348#issuecomment-) | 3 | 3次提交 |
| [#9342](https://github.com/NVIDIA/TensorRT-LLM/pull/9342) | [TRTLLM-5971][feat] Integrate helix parallelism | 5 | • CI检查失败 (4次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/9342#issuecomment-)<br>• Review Changes Requested (1次) - [Reviews](https://github.com/NVIDIA/TensorRT-LLM/pull/9342/files) | 1 | 1次提交 |
| [#9336](https://github.com/NVIDIA/TensorRT-LLM/pull/9336) | [https://nvbugs/5676748][fix] Fix mismatched nvfp4 gemm sf shape. | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/9336#issuecomment-) | 1 | 1次提交 |
| [#9320](https://github.com/NVIDIA/TensorRT-LLM/pull/9320) | [None][chore] Revise the description of enable_autotuner. | 0 | - | 1 | [`1854195`](https://github.com/NVIDIA/TensorRT-LLM/commit/185419558edbfb7c65bd40ee1b37e101482cf090) |
| [#9290](https://github.com/NVIDIA/TensorRT-LLM/pull/9290) | [None][infra] Add fallback when get wheel from build stage is fail | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/9290#issuecomment-) | 5 | 5次提交 |
| [#9210](https://github.com/NVIDIA/TensorRT-LLM/pull/9210) | [https://nvbugs/5590408][fix] Exclude num of draft tokens from mMaxSeqLenKv | 0 | - | 3 | 3次提交 |
| [#9209](https://github.com/NVIDIA/TensorRT-LLM/pull/9209) | [None][ci] split speculative test case into several small cases | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/9209#issuecomment-) | 2 | 2次提交 |
| [#9206](https://github.com/NVIDIA/TensorRT-LLM/pull/9206) | [https://nvbugs/5652552][fix] cherry-pick add printing for llm args | 0 | - | 2 | 2次提交 |
| [#9204](https://github.com/NVIDIA/TensorRT-LLM/pull/9204) | [None] [tests] Unwaive wide ep related tests | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/9204#issuecomment-) | 2 | 2次提交 |
| [#9201](https://github.com/NVIDIA/TensorRT-LLM/pull/9201) | [https://nvbugs/5649826][fix] Unwaive test test_llm_commandr_plus_4gpus_summary | 0 | - | 2 | 2次提交 |
| [#9195](https://github.com/NVIDIA/TensorRT-LLM/pull/9195) | [None][feature] AutoDeploy: tighter MoE UT thresholds | 0 | - | 1 | 1次提交 |
| [#9171](https://github.com/NVIDIA/TensorRT-LLM/pull/9171) | [None] [fix] Fix missing ActivationType issue | 5 | • CI检查失败 (5次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/9171#issuecomment-) | 4 | 4次提交 |
| [#9145](https://github.com/NVIDIA/TensorRT-LLM/pull/9145) | [https://nvbugs/5647400] [fix] Enlarged the AllReduce workspace size to 64MB. Ad | 7 | • CI检查失败 (7次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/9145#issuecomment-) | 16 | 16次提交 |
| [#9126](https://github.com/NVIDIA/TensorRT-LLM/pull/9126) | [None] [fix] Disable UCC as WAR to MPI allgather issue before NGC PyTorch 25.12  | 0 | - | 2 | 2次提交 |
| [#9122](https://github.com/NVIDIA/TensorRT-LLM/pull/9122) | [None][chore] Add placement test for ray executor | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/9122#issuecomment-) | 1 | [`ff549a3`](https://github.com/NVIDIA/TensorRT-LLM/commit/ff549a314b03564c6dba19a8c84520bee995760c) |
| [#9084](https://github.com/NVIDIA/TensorRT-LLM/pull/9084) | [None][infra] Lock generation pipeline update | 0 | - | 3 | 3次提交 |
| [#9063](https://github.com/NVIDIA/TensorRT-LLM/pull/9063) | [TRTLLM-9018][infra] add mirror for Build-Docker-Images stage | 0 | - | 2 | 2次提交 |
| [#9033](https://github.com/NVIDIA/TensorRT-LLM/pull/9033) | [TRTLLM-9073][doc] Add the missing content for model support section and fix… | 0 | - | 1 | 1次提交 |
| [#9001](https://github.com/NVIDIA/TensorRT-LLM/pull/9001) | [https://nvbugs/5637037][fix] Update unwaive list. | 5 | • CI检查失败 (5次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/9001#issuecomment-) | 1 | 1次提交 |
| [#8987](https://github.com/NVIDIA/TensorRT-LLM/pull/8987) | [None][infra] Update allowed list 2025.11.06 | 0 | - | 1 | 1次提交 |
| [#8970](https://github.com/NVIDIA/TensorRT-LLM/pull/8970) | [https://nvbugs/5633340][fix] kill processes properly after test | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8970#issuecomment-) | 2 | 2次提交 |
| [#8950](https://github.com/NVIDIA/TensorRT-LLM/pull/8950) | [None][perf] Adjust select_alltoall_method_type. | 7 | • CI检查失败 (7次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8950#issuecomment-) | 9 | 9次提交 |
| [#8914](https://github.com/NVIDIA/TensorRT-LLM/pull/8914) | [None][fix] Remove duplicated test waives | 0 | - | 1 | 1次提交 |
| [#8913](https://github.com/NVIDIA/TensorRT-LLM/pull/8913) | [None][feat] add swapsMmaAb sparseMla kernels | 4 | • CI检查失败 (4次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8913#issuecomment-) | 1 | 1次提交 |
| [#8901](https://github.com/NVIDIA/TensorRT-LLM/pull/8901) | [https://nvbugs/5630700][chore] Unwaive Qwen3_235B_A22B test | 0 | - | 1 | 1次提交 |
| [#8883](https://github.com/NVIDIA/TensorRT-LLM/pull/8883) | [https://nvbugs/5467531][fix] Fix moe test and wide ep fake impl | 3 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8883#issuecomment-)<br>• Review Changes Requested (1次) - [Reviews](https://github.com/NVIDIA/TensorRT-LLM/pull/8883/files) | 1 | 1次提交 |
| [#8877](https://github.com/NVIDIA/TensorRT-LLM/pull/8877) | [TRTLLM-9080][infra] upgrade tritonserver DLFW 25.10 | 5 | • CI检查失败 (5次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8877#issuecomment-) | 4 | 4次提交 |
| [#8869](https://github.com/NVIDIA/TensorRT-LLM/pull/8869) | [TRTLLM-9073/9087][doc] Add the missing content for model support section and fi | 0 | - | 2 | 2次提交 |
| [#8868](https://github.com/NVIDIA/TensorRT-LLM/pull/8868) | [None][infra] Modify wheel path from cuda13/ to dlfw/ | 0 | - | 1 | 1次提交 |
| [#8838](https://github.com/NVIDIA/TensorRT-LLM/pull/8838) | [TRTLLM-8994][infra] upgrade to DLFW 25.10 and pytorch 2.9.0 / triton 3.5.0 | 5 | • CI检查失败 (5次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8838#issuecomment-) | 4 | 4次提交 |
| [#8812](https://github.com/NVIDIA/TensorRT-LLM/pull/8812) | [#8763][feature] AutoDeploy: configurable dtype for caching | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8812#issuecomment-) | 2 | 2次提交 |
| [#8800](https://github.com/NVIDIA/TensorRT-LLM/pull/8800) | [TRTLLM-9000][feat] Add multi-node Perf Tests into CI | 5 | • CI检查失败 (5次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8800#issuecomment-) | 1 | 1次提交 |
| [#8776](https://github.com/NVIDIA/TensorRT-LLM/pull/8776) | [None][feat] Add benchmark to DeepConf | 3 | • CI检查失败 (3次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8776#issuecomment-) | 1 | 1次提交 |
| [#8759](https://github.com/NVIDIA/TensorRT-LLM/pull/8759) | [None][infra] Waive failed tests on main 10/29 | 0 | - | 1 | 1次提交 |
| [#8750](https://github.com/NVIDIA/TensorRT-LLM/pull/8750) | [None][fix] Fix KV cache clearing with KV Connector API | 6 | • CI检查失败 (6次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8750#issuecomment-) | 9 | 9次提交 |
| [#8728](https://github.com/NVIDIA/TensorRT-LLM/pull/8728) | [None][feat] Integrate MnnvlThroughput into TRTLLM MoE. | 3 | • CI检查失败 (3次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8728#issuecomment-) | 15 | 15次提交 |
| [#8724](https://github.com/NVIDIA/TensorRT-LLM/pull/8724) | [TRTLLM-8971][infra] Update gpu key for B300/GB300 | 3 | • CI检查失败 (3次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8724#issuecomment-) | 3 | 3次提交 |
| [#8678](https://github.com/NVIDIA/TensorRT-LLM/pull/8678) | [TRTLLM-8933][chore] remove unused update_executor_config function | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8678#issuecomment-) | 2 | 2次提交 |
| [#8668](https://github.com/NVIDIA/TensorRT-LLM/pull/8668) | [None][infra] Waive failed case on main 10/26 | 0 | - | 1 | 1次提交 |
| [#8665](https://github.com/NVIDIA/TensorRT-LLM/pull/8665) | [None][doc] Clarify the perf best practice and supported hardware for gptoss | 0 | - | 4 | 4次提交 |
| [#8657](https://github.com/NVIDIA/TensorRT-LLM/pull/8657) | [None][autodeploy] minor refactor to rmsnorm transforms | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8657#issuecomment-) | 3 | 3次提交 |
| [#8625](https://github.com/NVIDIA/TensorRT-LLM/pull/8625) | [https://nvbugs/5593199][test] Enhance beam search tests deterministic dummy mod | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8625#issuecomment-) | 2 | 2次提交 |
| [#8613](https://github.com/NVIDIA/TensorRT-LLM/pull/8613) | [None][infra] Disable rtxpro6000 stages due to nodes will be offline | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8613#issuecomment-) | 1 | 1次提交 |
| [#8611](https://github.com/NVIDIA/TensorRT-LLM/pull/8611) | [https://nvbugs/5587456][fix] Remove multimodal test cases using TRT backend | 0 | - | 1 | 1次提交 |
| [#8601](https://github.com/NVIDIA/TensorRT-LLM/pull/8601) | [None] [test] Add MNNVL AlltoAll tests to pre-merge | 4 | • CI检查失败 (4次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8601#issuecomment-) | 1 | 1次提交 |
| [#8600](https://github.com/NVIDIA/TensorRT-LLM/pull/8600) | [TRTLLM-8836][chore] Create ModelEngine from LlmArgs | 7 | • CI检查失败 (7次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8600#issuecomment-) | 22 | 22次提交 |
| [#8585](https://github.com/NVIDIA/TensorRT-LLM/pull/8585) | [None][infra] Fix slurm exitcode | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8585#issuecomment-) | 5 | 5次提交 |
| [#8561](https://github.com/NVIDIA/TensorRT-LLM/pull/8561) | [TRTLLM-8817][chore] Set default value of KvCacheConfig.free_gpu_memory_fraction | 6 | • CI检查失败 (6次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8561#issuecomment-) | 5 | 5次提交 |
| [#8546](https://github.com/NVIDIA/TensorRT-LLM/pull/8546) | [https://nvbugs/5576192][fix] Unwaive the test for test_weight_only_quant_gemm. | 0 | - | 1 | 1次提交 |
| [#8534](https://github.com/NVIDIA/TensorRT-LLM/pull/8534) | [None][chore] add precommit hook to remove redundant tab and white space | 0 | - | 1 | 1次提交 |
| [#8523](https://github.com/NVIDIA/TensorRT-LLM/pull/8523) | [TRTLLM-7835][test] add default sample config for perf test | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8523#issuecomment-) | 3 | 3次提交 |
| [#8509](https://github.com/NVIDIA/TensorRT-LLM/pull/8509) | [TRTLLM-6756][feat] Add Beam Search to TorchSampler | 7 | • CI检查失败 (7次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8509#issuecomment-) | 17 | 17次提交 |
| [#8440](https://github.com/NVIDIA/TensorRT-LLM/pull/8440) | [https://nvbugs/5515753][ci] Add NCCL_DEBUG=INFO flag to collect more… | 6 | • CI检查失败 (6次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8440#issuecomment-) | 4 | 4次提交 |
| [#8437](https://github.com/NVIDIA/TensorRT-LLM/pull/8437) | [https://nvbugs/5568676][fix] Remove test waive | 0 | - | 1 | 1次提交 |
| [#8408](https://github.com/NVIDIA/TensorRT-LLM/pull/8408) | [None][chore] Isolate several intermittent cases | 0 | - | 1 | 1次提交 |
| [#8392](https://github.com/NVIDIA/TensorRT-LLM/pull/8392) | [None][feat] Add fmha_v2 kernel for head_dim=80 and sm=100 to support VLM | 0 | - | 1 | 1次提交 |
| [#8355](https://github.com/NVIDIA/TensorRT-LLM/pull/8355) | [None][fix] Fix is_post_quant_all2all_supported for MNNVL | 0 | - | 1 | 1次提交 |
| [#8353](https://github.com/NVIDIA/TensorRT-LLM/pull/8353) | [https://nvbugs/5541494] [fix] Remove waivers | 0 | - | 4 | 4次提交 |
| [#8349](https://github.com/NVIDIA/TensorRT-LLM/pull/8349) | [None][ci] waive several rpc tests | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8349#issuecomment-) | 1 | 1次提交 |
| [#8344](https://github.com/NVIDIA/TensorRT-LLM/pull/8344) | [https://nvbugs/5534705][fix] Skip unnecessary CUDA graph capture (#8… | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8344#issuecomment-) | 1 | 1次提交 |
| [#8332](https://github.com/NVIDIA/TensorRT-LLM/pull/8332) | [None][feat] Add FP8 rowwise GEMMs for B200 | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8332#issuecomment-) | 5 | 5次提交 |
| [#8327](https://github.com/NVIDIA/TensorRT-LLM/pull/8327) | [None][fix] workaround for numexpr issue | 0 | - | 1 | 1次提交 |
| [#8323](https://github.com/NVIDIA/TensorRT-LLM/pull/8323) | [None] [blog] Scaling Expert Parallelism in TensorRT LLM (Part 3: Pushing the Pe | 0 | - | 4 | 4次提交 |
| [#8322](https://github.com/NVIDIA/TensorRT-LLM/pull/8322) | [https://nvbugs/5537738][fix] Add fp8 post-quant allgather support to release 1. | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8322#issuecomment-) | 1 | 1次提交 |
| [#8321](https://github.com/NVIDIA/TensorRT-LLM/pull/8321) | [None][test] Add post merge test for Seed-OSS-36B-Instruct | 0 | - | 3 | 3次提交 |
| [#8319](https://github.com/NVIDIA/TensorRT-LLM/pull/8319) | [TRTLLM-8435][infra] Test existing rtxpro6000 stages on rtxpro6000d | 7 | • CI检查失败 (7次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8319#issuecomment-) | 23 | 23次提交 |
| [#8307](https://github.com/NVIDIA/TensorRT-LLM/pull/8307) | [https://nvbugs/5550671][fix] fix disagg-serving multinodes test failure | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8307#issuecomment-) | 2 | 2次提交 |
| [#8302](https://github.com/NVIDIA/TensorRT-LLM/pull/8302) | [TRTLLM-8511][feat] Add update_weights and sleep_wakeup support for rl integrati | 4 | • CI检查失败 (4次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8302#issuecomment-) | 16 | [`9416923`](https://github.com/NVIDIA/TensorRT-LLM/commit/9416923faa5917f8a1d76f47bfe3273143008c4a), [`c7b73fd`](https://github.com/NVIDIA/TensorRT-LLM/commit/c7b73fd709f35e1c99b1778ecb7051ba0f109a7b), [`0d6339c`](https://github.com/NVIDIA/TensorRT-LLM/commit/0d6339c6e43ee692364b96be2834fb85c5542ba8), [`8579c29`](https://github.com/NVIDIA/TensorRT-LLM/commit/8579c297f3d039e74c1c02b24c6884cad453b00b), [`516408c`](https://github.com/NVIDIA/TensorRT-LLM/commit/516408cadcddf31ff5194a51eb032fddb66b3bfd), [`cc48567`](https://github.com/NVIDIA/TensorRT-LLM/commit/cc48567df1b589e9abd16cb614a343e905dec3fb), [`016b402`](https://github.com/NVIDIA/TensorRT-LLM/commit/016b402f90599566652c6224f473318d4db91107), [`f468ab4`](https://github.com/NVIDIA/TensorRT-LLM/commit/f468ab4acf10553809f28c256cae055df8fc0be2), [`d7481f8`](https://github.com/NVIDIA/TensorRT-LLM/commit/d7481f8f31dac52081524d4ba93c2756945b7d46), [`9400016`](https://github.com/NVIDIA/TensorRT-LLM/commit/940001658f3fb146b50e0f6000d67087a5af02c9)... (+6) |
| [#8294](https://github.com/NVIDIA/TensorRT-LLM/pull/8294) | [https://nvbugs/5404000][fix] Ensure consistency between firstTokenTime and last | 0 | - | 1 | 1次提交 |
| [#8289](https://github.com/NVIDIA/TensorRT-LLM/pull/8289) | [None][chore] Update disagg benchmark configs | 0 | - | 3 | [`1a2accf`](https://github.com/NVIDIA/TensorRT-LLM/commit/1a2accfe5d5b25562ed32f5f8a21e45b8ecef33f), [`de8e090`](https://github.com/NVIDIA/TensorRT-LLM/commit/de8e0904e85d1e47a53f0fd56aed0960e689fdb8), [`1c295e4`](https://github.com/NVIDIA/TensorRT-LLM/commit/1c295e4a2ea7234dbc1a4ac9dafe30bd1804a5d8) |
| [#8267](https://github.com/NVIDIA/TensorRT-LLM/pull/8267) | [None][infra] Remove WAR code for GH200 node | 0 | - | 1 | 1次提交 |
| [#8266](https://github.com/NVIDIA/TensorRT-LLM/pull/8266) | [None][infra] Remove WAR code for GH200 node | 0 | - | 1 | 1次提交 |
| [#8261](https://github.com/NVIDIA/TensorRT-LLM/pull/8261) | [None][feat] Add torch compile support for cuda core GEMM OP | 0 | - | 2 | 2次提交 |
| [#8230](https://github.com/NVIDIA/TensorRT-LLM/pull/8230) | [None][infra] Waive failed tests on main 10/09 | 0 | - | 2 | 2次提交 |
| [#8212](https://github.com/NVIDIA/TensorRT-LLM/pull/8212) | [TRTLLM-8246][test] add multimodal kvcache+chunked_prefil cases in to QA test li | 0 | - | 1 | 1次提交 |
| [#8206](https://github.com/NVIDIA/TensorRT-LLM/pull/8206) | [https://nvbugs/5563469][fix] Temporarily disable test_nemotron_nano_8b_lora_tor | 4 | • CI检查失败 (4次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8206#issuecomment-) | 1 | 1次提交 |
| [#8185](https://github.com/NVIDIA/TensorRT-LLM/pull/8185) | [None][chore] Waive tests failing on release/1.1 post merge | 0 | - | 1 | 1次提交 |
| [#8174](https://github.com/NVIDIA/TensorRT-LLM/pull/8174) | [TRTLLM-7769][chore] document the role of 'd2t' | 0 | - | 1 | 1次提交 |
| [#8167](https://github.com/NVIDIA/TensorRT-LLM/pull/8167) | [https://nvbugs/5503138] [fix] Remove compile warnings | 0 | - | 1 | [`483a466`](https://github.com/NVIDIA/TensorRT-LLM/commit/483a4668b250348261e52c36fbcd98254a05be56) |
| [#8112](https://github.com/NVIDIA/TensorRT-LLM/pull/8112) | [None][fix] fix patchelf version issue | 0 | - | 1 | 1次提交 |
| [#8099](https://github.com/NVIDIA/TensorRT-LLM/pull/8099) | [#7588][feat] lock gpu clocks in test_perf.py to reliably detect perf regression | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8099#issuecomment-) | 2 | 2次提交 |
| [#8081](https://github.com/NVIDIA/TensorRT-LLM/pull/8081) | [TRTLLM-6239][feat] add test cases into QA test list | 0 | - | 1 | 1次提交 |
| [#8063](https://github.com/NVIDIA/TensorRT-LLM/pull/8063) | [https://nvbugs/5510879][fix] Fix pytorch & TRT-python flows fused LoRA adapter  | 6 | • CI检查失败 (6次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8063#issuecomment-) | 16 | 16次提交 |
| [#8059](https://github.com/NVIDIA/TensorRT-LLM/pull/8059) | [None][fix] Fix TRT-python multi LoRA TP=2 test arguments | 0 | - | 1 | 1次提交 |
| [#8024](https://github.com/NVIDIA/TensorRT-LLM/pull/8024) | [TRTLLM-8238][feat] Add EVS support for nano-v2-vlm | 5 | • CI检查失败 (5次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/8024#issuecomment-) | 3 | 3次提交 |
| [#8010](https://github.com/NVIDIA/TensorRT-LLM/pull/8010) | [None][ci] Waive test_mm_encoder_standalone.py::test_multi_request_batch_chat[ll | 0 | - | 1 | 1次提交 |
| [#7977](https://github.com/NVIDIA/TensorRT-LLM/pull/7977) | [TRTLLM-6748][feat] add PDL support for more kernels | 7 | • CI检查失败 (7次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/7977#issuecomment-) | 3 | 3次提交 |
| [#7965](https://github.com/NVIDIA/TensorRT-LLM/pull/7965) | [https://nvbugs/5451740][fix] Add DP padding back on SM120 | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/7965#issuecomment-) | 5 | 5次提交 |
| [#7951](https://github.com/NVIDIA/TensorRT-LLM/pull/7951) | [TRTLLM-7999][infra] Add B300/GB300 single gpu test | 3 | • CI检查失败 (3次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/7951#issuecomment-) | 2 | 2次提交 |
| [#7917](https://github.com/NVIDIA/TensorRT-LLM/pull/7917) | [None] [feat] Update disagg gen-only benchmark. | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/7917#issuecomment-) | 7 | 7次提交 |
| [#7900](https://github.com/NVIDIA/TensorRT-LLM/pull/7900) | [https://nvbugs/5351244][fix] CHERRY-PICK test_mpi_session (#7501) | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/7900#issuecomment-) | 1 | 1次提交 |
| [#7893](https://github.com/NVIDIA/TensorRT-LLM/pull/7893) | [TRTLLM-8209][feat] Support new structural tag API (upgrade XGrammar to 0.1.25) | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/7893#issuecomment-) | 4 | 4次提交 |
| [#7841](https://github.com/NVIDIA/TensorRT-LLM/pull/7841) | [None][chore] Add failed cases into waives.txt | 0 | - | 2 | 2次提交 |
| [#7837](https://github.com/NVIDIA/TensorRT-LLM/pull/7837) | [None][doc] Replace the main in the examples' link with commit id. | 0 | - | 1 | 1次提交 |
| [#7808](https://github.com/NVIDIA/TensorRT-LLM/pull/7808) | [https://nvbugs/5513423][fix] Correctly respect min_tokens in PyTorch Workflow | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/7808#issuecomment-) | 3 | 3次提交 |
| [#7770](https://github.com/NVIDIA/TensorRT-LLM/pull/7770) | [#5860][feat] Add ModelOPT INT4 awq fake quant support in AutoDeploy | 6 | • CI检查失败 (6次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/7770#issuecomment-) | 4 | 4次提交 |
| [#7757](https://github.com/NVIDIA/TensorRT-LLM/pull/7757) | [TRTLLM-6286] [perf] Add NoSmem epilogue schedule and dynamic cluster shape for  | 5 | • CI检查失败 (5次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/7757#issuecomment-) | 11 | 11次提交 |
| [#7724](https://github.com/NVIDIA/TensorRT-LLM/pull/7724) | [https://nvbugs/5355219][fix] Fix trtllm moe backend  test config and Qwen3 MoE  | 0 | - | 1 | 1次提交 |
| [#7723](https://github.com/NVIDIA/TensorRT-LLM/pull/7723) | [TRTLLM-7918][feat] Support kvcache reuse and chunk prefill for phi4mm | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/7723#issuecomment-) | 1 | 1次提交 |
| [#7720](https://github.com/NVIDIA/TensorRT-LLM/pull/7720) | [None][fix] waive hang tests on main | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/7720#issuecomment-) | 1 | 1次提交 |
| [#7696](https://github.com/NVIDIA/TensorRT-LLM/pull/7696) | [None][doc] Add labels description note into llm api section | 0 | - | 1 | 1次提交 |
| [#7686](https://github.com/NVIDIA/TensorRT-LLM/pull/7686) | [https://nvbugs/5471108][chore] Unwaiving disagg acc test | 4 | • CI检查失败 (4次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/7686#issuecomment-) | 1 | 1次提交 |
| [#7678](https://github.com/NVIDIA/TensorRT-LLM/pull/7678) | [None][test] add test for min_tokens | 0 | - | 1 | 1次提交 |
| [#7639](https://github.com/NVIDIA/TensorRT-LLM/pull/7639) | [None][fix] add the missing import raised by #7607 | 0 | - | 1 | 1次提交 |
| [#7635](https://github.com/NVIDIA/TensorRT-LLM/pull/7635) | [#7308] [feat] AutoDeploy: graph-less transformers mode for HF | 0 | - | 25 | 25次提交 |
| [#7628](https://github.com/NVIDIA/TensorRT-LLM/pull/7628) | [TRTLLM-7410][feat] Enable KV cache reuse and chunked prefill for mistral3.1 | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/7628#issuecomment-) | 1 | 1次提交 |
| [#7616](https://github.com/NVIDIA/TensorRT-LLM/pull/7616) | [https://nvbugs/5505402] [fix] Disable deep_gemm for Qwen3 QKNormRoPEAttention a | 3 | • CI检查失败 (3次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/7616#issuecomment-) | 1 | 1次提交 |
| [#7607](https://github.com/NVIDIA/TensorRT-LLM/pull/7607) | [None][chore] Mass integration of release/1.0 - 4th (release/1.0 doc change main | 0 | - | 3 | 3次提交 |
| [#7604](https://github.com/NVIDIA/TensorRT-LLM/pull/7604) | [https://nvbugs/5506683][fix] adjust the CI | 0 | - | 1 | 1次提交 |
| [#7598](https://github.com/NVIDIA/TensorRT-LLM/pull/7598) | [None][chore] Make use_low_precision_moe_combine as a llm arg | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/7598#issuecomment-) | 2 | 2次提交 |
| [#7585](https://github.com/NVIDIA/TensorRT-LLM/pull/7585) | [None][ci] Waive qwen3 test for accuracy bug in https://nvbugs/5505402 | 0 | - | 1 | 1次提交 |
| [#7568](https://github.com/NVIDIA/TensorRT-LLM/pull/7568) | [TRTLLM-4629] [feat] Add support of CUDA13 and sm103 devices | 0 | - | 108 | 108次提交 |
| [#7563](https://github.com/NVIDIA/TensorRT-LLM/pull/7563) | [TRTLLM-7918][feat] Support kvcache reuse for phi4mm | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/7563#issuecomment-) | 1 | 1次提交 |
| [#7538](https://github.com/NVIDIA/TensorRT-LLM/pull/7538) | [None][fix] Fix a typo in the Slurm CI codes (#7485) | 0 | - | 1 | 1次提交 |
| [#7534](https://github.com/NVIDIA/TensorRT-LLM/pull/7534) | [None][fix] Update DG commit | 0 | - | 1 | 1次提交 |
| [#7505](https://github.com/NVIDIA/TensorRT-LLM/pull/7505) | [https://nvbugs/5494698][fix] skip gemma3 27b on blackwell | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/7505#issuecomment-) | 2 | 2次提交 |
| [#7421](https://github.com/NVIDIA/TensorRT-LLM/pull/7421) | [None][test] auto reuse torch empty cache on qa test | 0 | - | 1 | 1次提交 |
| [#7413](https://github.com/NVIDIA/TensorRT-LLM/pull/7413) | [TRTLLM-6643][feat] Add DeepSeek-v3-0324 e2e torch test | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/7413#issuecomment-) | 10 | 10次提交 |
| [#7409](https://github.com/NVIDIA/TensorRT-LLM/pull/7409) | [None] [fix] Fix nsys in slurm scripts | 0 | - | 6 | 6次提交 |
| [#7366](https://github.com/NVIDIA/TensorRT-LLM/pull/7366) | [https://nvbugs/5485593][fix] improve accuracy/test_disaggregated_serving.py | 0 | - | 2 | 2次提交 |
| [#7362](https://github.com/NVIDIA/TensorRT-LLM/pull/7362) | [None][doc] update architecture overview doc | 0 | - | 1 | 1次提交 |
| [#7360](https://github.com/NVIDIA/TensorRT-LLM/pull/7360) | [TRTLLM-7410][feat] Support hashing and KV cache reuse for videos | 0 | - | 6 | 6次提交 |
| [#7358](https://github.com/NVIDIA/TensorRT-LLM/pull/7358) | [None] [doc] Update DeepSeek example doc | 0 | - | 2 | 2次提交 |
| [#7333](https://github.com/NVIDIA/TensorRT-LLM/pull/7333) | [None][ci] skip TestGPTOSS | 0 | - | 2 | 2次提交 |
| [#7286](https://github.com/NVIDIA/TensorRT-LLM/pull/7286) | [https://nvbugs/5378031] [feat] W4A8 AWQ MoE supports Per Expert Pre-quant Scale | 4 | • CI检查失败 (4次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/7286#issuecomment-) | 3 | 3次提交 |
| [#7277](https://github.com/NVIDIA/TensorRT-LLM/pull/7277) | [TRTLLM-7408][feat] Wrap MOE with custom op. | 7 | • CI检查失败 (7次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/7277#issuecomment-) | 1 | [`b0dcd1e`](https://github.com/NVIDIA/TensorRT-LLM/commit/b0dcd1ee64fb39d83f9e8c0066db1f0f5e453351) |
| [#7258](https://github.com/NVIDIA/TensorRT-LLM/pull/7258) | [None][infra] Waive failed cases for release/1.0 08/26 | 0 | - | 1 | 1次提交 |
| [#7252](https://github.com/NVIDIA/TensorRT-LLM/pull/7252) | [None][docs] refine docs for accuracy evaluation of gpt-oss models | 0 | - | 2 | 2次提交 |
| [#7238](https://github.com/NVIDIA/TensorRT-LLM/pull/7238) | [None][fix] Remove and fuse some element-wise ops in the ds-r1-fp8 model | 0 | - | 2 | 2次提交 |
| [#7233](https://github.com/NVIDIA/TensorRT-LLM/pull/7233) | [None][doc] Update autodeploy README.md, deprecate lm_eval in examples folder | 0 | - | 2 | 2次提交 |
| [#7232](https://github.com/NVIDIA/TensorRT-LLM/pull/7232) | [None][feat] Add logging for OAI disagg server | 2 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/7232#issuecomment-)<br>• Review Changes Requested (1次) - [Reviews](https://github.com/NVIDIA/TensorRT-LLM/pull/7232/files) | 2 | 2次提交 |
| [#7211](https://github.com/NVIDIA/TensorRT-LLM/pull/7211) | [None][test] add kv cache size in bench metric and fix failed cases | 0 | - | 1 | 1次提交 |
| [#7210](https://github.com/NVIDIA/TensorRT-LLM/pull/7210) | [None][fix] fix log_once usage | 0 | - | 1 | 1次提交 |
| [#7179](https://github.com/NVIDIA/TensorRT-LLM/pull/7179) | [None][chore] Enable auto deploy accuracy test in CI | 4 | • CI检查失败 (4次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/7179#issuecomment-) | 6 | 6次提交 |
| [#7173](https://github.com/NVIDIA/TensorRT-LLM/pull/7173) | [https://nvbugs/5467062][fix] pass logitsPostProcessorBatched by reference | 3 | • CI检查失败 (3次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/7173#issuecomment-) | 1 | [`0743b35`](https://github.com/NVIDIA/TensorRT-LLM/commit/0743b3594439353426c5b830b81042f122f7bab6) |
| [#7171](https://github.com/NVIDIA/TensorRT-LLM/pull/7171) | [None][chore] Mass integration of release/1.0 - 2nd | 6 | • CI检查失败 (6次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/7171#issuecomment-) | 33 | 33次提交 |
| [#7143](https://github.com/NVIDIA/TensorRT-LLM/pull/7143) | [TRTLLM-7321][doc] Add GPT-OSS Deployment Guide into official doc site | 0 | - | 2 | 2次提交 |
| [#7070](https://github.com/NVIDIA/TensorRT-LLM/pull/7070) | [None][fix] fix scaffolding dynasor test | 0 | - | 1 | 1次提交 |
| [#7041](https://github.com/NVIDIA/TensorRT-LLM/pull/7041) | [TRTLLM-7153] [feat] Move stop_criteria to sample_async | 0 | - | 33 | 33次提交 |
| [#7013](https://github.com/NVIDIA/TensorRT-LLM/pull/7013) | [None][feat] Skip prefetching consolidated safetensors when appropriate | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/7013#issuecomment-) | 1 | 1次提交 |
| [#7008](https://github.com/NVIDIA/TensorRT-LLM/pull/7008) | [https://nvbugs/5462007][ci] Unwaive Mistral Small 3.1 FP8 test | 0 | - | 1 | 1次提交 |
| [#7004](https://github.com/NVIDIA/TensorRT-LLM/pull/7004) | [https://nvbugs/5444937][chore] Fixing KV events tests | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/7004#issuecomment-) | 3 | 3次提交 |
| [#7003](https://github.com/NVIDIA/TensorRT-LLM/pull/7003) | [None][fix] Fix build of tritonbuild/tritonrelease image | 1 | • Review Changes Requested (1次) - [Reviews](https://github.com/NVIDIA/TensorRT-LLM/pull/7003/files) | 5 | 5次提交 |
| [#6996](https://github.com/NVIDIA/TensorRT-LLM/pull/6996) | [https://nvbugs/5458874][fix] Fix Nemotron-H flaky CUDA graph / overlap schedule | 0 | - | 2 | 2次提交 |
| [#6990](https://github.com/NVIDIA/TensorRT-LLM/pull/6990) | [https://nvbugs/5450074][fix] Reduce the device memory requirements for testing | 0 | - | 1 | 1次提交 |
| [#6984](https://github.com/NVIDIA/TensorRT-LLM/pull/6984) | [https://nvbugs/5453827][fix] Fix RPATH of th_common shared library to find pip- | 3 | • CI检查失败 (3次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/6984#issuecomment-) | 3 | 3次提交 |
| [#6945](https://github.com/NVIDIA/TensorRT-LLM/pull/6945) | [None][infra] update feature_combination_matrix of disaggregated and Eagle3 | 0 | - | 1 | 1次提交 |
| [#6944](https://github.com/NVIDIA/TensorRT-LLM/pull/6944) | [None][chore] unwaive test_disaggregated_genbs1 | 0 | - | 1 | 1次提交 |
| [#6940](https://github.com/NVIDIA/TensorRT-LLM/pull/6940) | [https://nvbugs/5448437][fix] fix some nixl tests | 0 | - | 2 | 2次提交 |
| [#6908](https://github.com/NVIDIA/TensorRT-LLM/pull/6908) | [None][doc] Update gpt-oss doc on MoE support matrix | 0 | - | 1 | 1次提交 |
| [#6896](https://github.com/NVIDIA/TensorRT-LLM/pull/6896) | [https://nvbugs/5394685][fix] using static scheduler 2CTA MLA as WAR for an accu | 0 | - | 1 | 1次提交 |
| [#6873](https://github.com/NVIDIA/TensorRT-LLM/pull/6873) | [https://nvbugs/5455651][fix] Make ngram use XQA attention on Blackwell | 0 | - | 3 | 3次提交 |
| [#6825](https://github.com/NVIDIA/TensorRT-LLM/pull/6825) | [None][fix] Fix python-only build that uses TRTLLM_USE_PRECOMPILED | 0 | - | 2 | 2次提交 |
| [#6796](https://github.com/NVIDIA/TensorRT-LLM/pull/6796) | [None] [chore] Mamba cache in separate file | 3 | • CI检查失败 (3次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/6796#issuecomment-) | 5 | 5次提交 |
| [#6794](https://github.com/NVIDIA/TensorRT-LLM/pull/6794) | [None] [feat] Enable run_post_quant_allgather for MoE TRTLLM backend | 8 | • CI检查失败 (8次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/6794#issuecomment-) | 1 | 1次提交 |
| [#6791](https://github.com/NVIDIA/TensorRT-LLM/pull/6791) | [None][infra] Unwaive an updated case to test | 0 | - | 1 | 1次提交 |
| [#6775](https://github.com/NVIDIA/TensorRT-LLM/pull/6775) | [None][feat] Enable gpt oss on DGX H100. | 0 | - | 2 | 2次提交 |
| [#6763](https://github.com/NVIDIA/TensorRT-LLM/pull/6763) | [None][chore] Find LLM_ROOT and LLM_BACKEND_ROOT dynamically | 0 | - | 2 | 2次提交 |
| [#6762](https://github.com/NVIDIA/TensorRT-LLM/pull/6762) | [TRTLLM-7025] [infra] Reorganize CODEOWNERS to rectify `examples` mapping | 0 | - | 2 | 2次提交 |
| [#6750](https://github.com/NVIDIA/TensorRT-LLM/pull/6750) | [TRTLLM-6633][feat] Padding for piecewise cudagraph | 0 | - | 2 | 2次提交 |
| [#6744](https://github.com/NVIDIA/TensorRT-LLM/pull/6744) | [https://nvbugs/5444624][fix] Fix LLM_ROOT in triton_backend build.sh | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/6744#issuecomment-) | 4 | 4次提交 |
| [#6739](https://github.com/NVIDIA/TensorRT-LLM/pull/6739) | [None][doc] Add doc for multimodal feature support matrix (#6619) | 0 | - | 1 | 1次提交 |
| [#6724](https://github.com/NVIDIA/TensorRT-LLM/pull/6724) | [None][doc] add legacy section for tensorrt engine | 5 | • CI检查失败 (5次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/6724#issuecomment-) | 3 | 3次提交 |
| [#6714](https://github.com/NVIDIA/TensorRT-LLM/pull/6714) | [https://nvbugs/5394409][feat] Support Mistral Small 3.1 multimodal in Triton Ba | 6 | • CI检查失败 (6次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/6714#issuecomment-) | 34 | 34次提交 |
| [#6704](https://github.com/NVIDIA/TensorRT-LLM/pull/6704) | [TRTLLM-6854][feat] Enable guided decoding with disagg serving | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/6704#issuecomment-) | 4 | 4次提交 |
| [#6701](https://github.com/NVIDIA/TensorRT-LLM/pull/6701) | [https://nvbugs/5441438][fix] Set correct draft length for the cuda graph dummy  | 3 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/6701#issuecomment-)<br>• Review Changes Requested (1次) - [Reviews](https://github.com/NVIDIA/TensorRT-LLM/pull/6701/files) | 2 | 2次提交 |
| [#6699](https://github.com/NVIDIA/TensorRT-LLM/pull/6699) | [https://nvbugs/5429689][fix] Fix mllama model structure update with transformer | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/6699#issuecomment-) | 1 | 1次提交 |
| [#6698](https://github.com/NVIDIA/TensorRT-LLM/pull/6698) | [TRTLLM-6853][feat] refactor deepseekv3 model | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/6698#issuecomment-) | 2 | 2次提交 |
| [#6660](https://github.com/NVIDIA/TensorRT-LLM/pull/6660) | [https://nvbugs/5409414][fix] fix Not registered specs | 3 | • CI检查失败 (3次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/6660#issuecomment-) | 3 | 3次提交 |
| [#6657](https://github.com/NVIDIA/TensorRT-LLM/pull/6657) | [None][chore] optimize kv cache transfer for context TEP and  gen DEP | 0 | - | 2 | 2次提交 |
| [#6651](https://github.com/NVIDIA/TensorRT-LLM/pull/6651) | [None][chore] Bump version to 1.1.0rc0 | 0 | - | 1 | 1次提交 |
| [#6597](https://github.com/NVIDIA/TensorRT-LLM/pull/6597) | [None][chore] Bump version to 1.0.0rc6 | 0 | - | 1 | 1次提交 |
| [#6592](https://github.com/NVIDIA/TensorRT-LLM/pull/6592) | [TRTLLM-6823][doc] Add checkpoint refactor docs | 0 | - | 3 | 3次提交 |
| [#6590](https://github.com/NVIDIA/TensorRT-LLM/pull/6590) | [None][chore] add missing tests to test list | 0 | - | 1 | 1次提交 |
| [#6563](https://github.com/NVIDIA/TensorRT-LLM/pull/6563) | [TRTLLM-6881][feat] Include attention dp rank info with KV cache events | 4 | • CI检查失败 (4次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/6563#issuecomment-) | 12 | 12次提交 |
| [#6555](https://github.com/NVIDIA/TensorRT-LLM/pull/6555) | [TRTLLM-6893][infra] fix Build Docker Image tag issue | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/6555#issuecomment-) | 3 | 3次提交 |
| [#6548](https://github.com/NVIDIA/TensorRT-LLM/pull/6548) | [None][feat] improve dataloading for benchmark_dataset by using batch… | 4 | • CI检查失败 (4次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/6548#issuecomment-) | 1 | 1次提交 |
| [#6542](https://github.com/NVIDIA/TensorRT-LLM/pull/6542) | [None][feat] Add test for speculative rejection sampler (2-model) | 3 | • CI检查失败 (3次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/6542#issuecomment-) | 8 | 8次提交 |
| [#6537](https://github.com/NVIDIA/TensorRT-LLM/pull/6537) | [https://nvbugs/5394392][fix] Enlarge scheduler capacity under disagg bs == 1 | 0 | - | 7 | 7次提交 |
| [#6494](https://github.com/NVIDIA/TensorRT-LLM/pull/6494) | [TRTLLM-6812][feat] Add standardized GitHub issue templates and disable blank is | 0 | - | 4 | 4次提交 |
| [#6472](https://github.com/NVIDIA/TensorRT-LLM/pull/6472) | [None][fix] fix: resolve GPU memory imbalance in concurrent weight loading | 4 | • CI检查失败 (4次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/6472#issuecomment-) | 7 | 7次提交 |
| [#6466](https://github.com/NVIDIA/TensorRT-LLM/pull/6466) | test: Add time logging for lora tests | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/6466#issuecomment-) | 1 | 1次提交 |
| [#6390](https://github.com/NVIDIA/TensorRT-LLM/pull/6390) | tests: add TestNemotronH cuda graph tests | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/6390#issuecomment-) | 4 | 4次提交 |
| [#6386](https://github.com/NVIDIA/TensorRT-LLM/pull/6386) | [None][infra] Enable accuracy test for eagle3 and chunked prefill | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/6386#issuecomment-) | 1 | 1次提交 |
| [#6338](https://github.com/NVIDIA/TensorRT-LLM/pull/6338) | [fix] Add trust_remote_code option to prepare_dataset. | 0 | - | 7 | 7次提交 |
| [#6333](https://github.com/NVIDIA/TensorRT-LLM/pull/6333) | test: [CI] Add failed cases into waives.txt | 0 | - | 1 | 1次提交 |
| [#6263](https://github.com/NVIDIA/TensorRT-LLM/pull/6263) | [TRTLLM-6654][feat] Add support for external multimodal embeddings | 3 | • CI检查失败 (3次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/6263#issuecomment-) | 15 | 15次提交 |
| [#6262](https://github.com/NVIDIA/TensorRT-LLM/pull/6262) | [https://nvbugs/5387771] fix deadlocks due to insufficient numSemaphores | 0 | - | 1 | 1次提交 |
| [#6223](https://github.com/NVIDIA/TensorRT-LLM/pull/6223) | [TRTLLM-6651][feat]  Enable Overlap scheduler +  Beam Search in TRTLLM Sampler | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/6223#issuecomment-) | 1 | 1次提交 |
| [#6181](https://github.com/NVIDIA/TensorRT-LLM/pull/6181) | [https://nvbugs/5393961][fix] record kv-cache size in MLACacheFormatter | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/6181#issuecomment-) | 1 | 1次提交 |
| [#6176](https://github.com/NVIDIA/TensorRT-LLM/pull/6176) | [Infra] - Waive failed tests in post-merge | 0 | - | 1 | 1次提交 |
| [#6161](https://github.com/NVIDIA/TensorRT-LLM/pull/6161) | [Doc][Qwen3] update qwen3 into support-matrix | 0 | - | 2 | 2次提交 |
| [#6147](https://github.com/NVIDIA/TensorRT-LLM/pull/6147) | [nvbug/5393888][nvbug/5393042] Always use `py_seq_slot` | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/6147#issuecomment-) | 3 | 3次提交 |
| [#6146](https://github.com/NVIDIA/TensorRT-LLM/pull/6146) | [fix]: Skip prompt length checking for generation only requests | 1 | • Review Changes Requested (1次) - [Reviews](https://github.com/NVIDIA/TensorRT-LLM/pull/6146/files) | 4 | 4次提交 |
| [#6139](https://github.com/NVIDIA/TensorRT-LLM/pull/6139) | [TRTLLM-6537][infra] extend multi-gpu tests related file list | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/6139#issuecomment-) | 1 | 1次提交 |
| [#6101](https://github.com/NVIDIA/TensorRT-LLM/pull/6101) | test: update max_beam_width to 1 due to torchsampler changes. | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/6101#issuecomment-) | 1 | 1次提交 |
| [#6097](https://github.com/NVIDIA/TensorRT-LLM/pull/6097) | [TRTLLM-1302][feat] Topk logprobs for TRT backend and top1 logprob for PyT backe | 7 | • CI检查失败 (7次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/6097#issuecomment-) | 10 | 10次提交 |
| [#6090](https://github.com/NVIDIA/TensorRT-LLM/pull/6090) | [None][chore] ucx establish connection with zmq | 4 | • CI检查失败 (4次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/6090#issuecomment-) | 5 | 5次提交 |
| [#6086](https://github.com/NVIDIA/TensorRT-LLM/pull/6086) | chore: Bump version to 1.0.0rc4 | 0 | - | 1 | 1次提交 |
| [#6082](https://github.com/NVIDIA/TensorRT-LLM/pull/6082) | [None] - Waive L0 tests | 0 | - | 1 | 1次提交 |
| [#6041](https://github.com/NVIDIA/TensorRT-LLM/pull/6041) | [nvbug/5347489][nvbug/5388036] increase timeout in disagg worker test | 0 | - | 1 | 1次提交 |
| [#6024](https://github.com/NVIDIA/TensorRT-LLM/pull/6024) | doc: Adding disaggregated serving page to features section for 1.0 docs [TRTLLM- | 0 | - | 7 | 7次提交 |
| [#6003](https://github.com/NVIDIA/TensorRT-LLM/pull/6003) | chore: [Breaking Change] Rename cuda_graph_config padding_enabled fie… | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/6003#issuecomment-) | 1 | 1次提交 |
| [#5997](https://github.com/NVIDIA/TensorRT-LLM/pull/5997) | [TRTLLM-5271][feat] best_of/n for pytorch workflow | 8 | • CI检查失败 (8次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/5997#issuecomment-) | 8 | 8次提交 |
| [#5995](https://github.com/NVIDIA/TensorRT-LLM/pull/5995) | [None][doc]: remove the outdated features which marked as Experimental | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/5995#issuecomment-) | 1 | 1次提交 |
| [#5994](https://github.com/NVIDIA/TensorRT-LLM/pull/5994) | chore: set default device to cpu on Multimodal models | 0 | - | 3 | 3次提交 |
| [#5931](https://github.com/NVIDIA/TensorRT-LLM/pull/5931) | [fix] Remove SpecConfig and fix thread leak issues | 0 | - | 3 | 3次提交 |
| [#5926](https://github.com/NVIDIA/TensorRT-LLM/pull/5926) | [nvbugs/5354884][fix] Update beam search workspace estimation to new upper bound | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/5926#issuecomment-) | 1 | 1次提交 |
| [#5919](https://github.com/NVIDIA/TensorRT-LLM/pull/5919) | Feat: Add vectorized loading for finalize kernel in MoE Trtllm backend | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/5919#issuecomment-) | 1 | 1次提交 |
| [#5906](https://github.com/NVIDIA/TensorRT-LLM/pull/5906) | tests: update sanity tests & fix tests | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/5906#issuecomment-) | 2 | 2次提交 |
| [#5885](https://github.com/NVIDIA/TensorRT-LLM/pull/5885) | [TRTLLM-6264] Fix flaky test_e2e.py::test_openai_lora | 0 | - | 9 | 9次提交 |
| [#5868](https://github.com/NVIDIA/TensorRT-LLM/pull/5868) | Fix: Enhance ModelConfig for kv cache size calculations | 6 | • CI检查失败 (6次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/5868#issuecomment-) | 5 | 5次提交 |
| [#5865](https://github.com/NVIDIA/TensorRT-LLM/pull/5865) | [https://nvbugs/5355316] fix: update torch.compile option to fix triton store_cu | 0 | - | 1 | 1次提交 |
| [#5840](https://github.com/NVIDIA/TensorRT-LLM/pull/5840) | doc: Update gb200 doc | 0 | - | 1 | 1次提交 |
| [#5821](https://github.com/NVIDIA/TensorRT-LLM/pull/5821) | fix: [https://nvbugs/5351130][https://nvbugs/5333654] Unwaive for bug 5351130 an | 0 | - | 1 | 1次提交 |
| [#5804](https://github.com/NVIDIA/TensorRT-LLM/pull/5804) | [TRTLLM-6081] doc: KV cache feature documentation | 0 | - | 12 | 12次提交 |
| [#5789](https://github.com/NVIDIA/TensorRT-LLM/pull/5789) | [nvbugs/5326453] Avoid nesting NCCL grouping in allgather OP | 0 | - | 6 | 6次提交 |
| [#5782](https://github.com/NVIDIA/TensorRT-LLM/pull/5782) | [NvBug 5362426] fix: Fix prompt adapter TP2 case | 0 | - | 2 | 2次提交 |
| [#5776](https://github.com/NVIDIA/TensorRT-LLM/pull/5776) | cherry pick #5416 | 0 | - | 1 | 1次提交 |
| [#5771](https://github.com/NVIDIA/TensorRT-LLM/pull/5771) | Refactor the rest routing part for the routing kernels in the MoE TRT-LLM backen | 5 | • CI检查失败 (4次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/5771#issuecomment-)<br>• Review Changes Requested (1次) - [Reviews](https://github.com/NVIDIA/TensorRT-LLM/pull/5771/files) | 1 | 1次提交 |
| [#5747](https://github.com/NVIDIA/TensorRT-LLM/pull/5747) | Update transformers to 4.53.0 | 4 | • CI检查失败 (4次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/5747#issuecomment-) | 1 | 1次提交 |
| [#5745](https://github.com/NVIDIA/TensorRT-LLM/pull/5745) | Add dummy all_reduce for kernel breakdown | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/5745#issuecomment-) | 6 | 6次提交 |
| [#5740](https://github.com/NVIDIA/TensorRT-LLM/pull/5740) | Waive tests : test_openai_lora, test_trtllm_serve_lora_example and test_openai_c | 0 | - | 1 | 1次提交 |
| [#5724](https://github.com/NVIDIA/TensorRT-LLM/pull/5724) | Cherry pick "[NVBUG:5355009] Modify check for fuse_fp4_quant on SM120 | 0 | - | 2 | 2次提交 |
| [#5706](https://github.com/NVIDIA/TensorRT-LLM/pull/5706) | chore [TRTLLM-6161]: add LLM speculative decoding example | 0 | - | 3 | 3次提交 |
| [#5705](https://github.com/NVIDIA/TensorRT-LLM/pull/5705) | [https://nvbugs/5365714] fix(scaffolding): use default LLM rather than trt backe | 0 | - | 1 | 1次提交 |
| [#5674](https://github.com/NVIDIA/TensorRT-LLM/pull/5674) | [Infra] - Waive failed cases on release/0.21 | 0 | - | 1 | 1次提交 |
| [#5667](https://github.com/NVIDIA/TensorRT-LLM/pull/5667) | [Infra] - Set default timeout to 1hr and remove some specific settings | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/5667#issuecomment-) | 1 | 1次提交 |
| [#5654](https://github.com/NVIDIA/TensorRT-LLM/pull/5654) | test: Validate and add accuracy& perf tests for Ministral-8B-Instruct[-FP8](pyto | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/5654#issuecomment-) | 4 | 4次提交 |
| [#5638](https://github.com/NVIDIA/TensorRT-LLM/pull/5638) | doc: Fix outdated config in DeepSeek best perf practice doc | 0 | - | 1 | 1次提交 |
| [#5634](https://github.com/NVIDIA/TensorRT-LLM/pull/5634) | [fix] Update to properly set cuda graphs in trtllm-bench overrides. | 0 | - | 19 | 19次提交 |
| [#5616](https://github.com/NVIDIA/TensorRT-LLM/pull/5616) | [TRTLLM-5826][feat] Support pytorch LoRA adapter eviction | 8 | • CI检查失败 (8次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/5616#issuecomment-) | 32 | 32次提交 |
| [#5615](https://github.com/NVIDIA/TensorRT-LLM/pull/5615) | [TRTLLM-5812][feat] support FP8 row-wise dense GEMM in torch flow | 0 | - | 11 | 11次提交 |
| [#5604](https://github.com/NVIDIA/TensorRT-LLM/pull/5604) | [ci] move eagle1 and medusa tests to post-merge | 0 | - | 1 | 1次提交 |
| [#5569](https://github.com/NVIDIA/TensorRT-LLM/pull/5569) | test: [CI] Add failed cases into waives.txt | 0 | - | 1 | 1次提交 |
| [#5536](https://github.com/NVIDIA/TensorRT-LLM/pull/5536) | [Infra] - Waive failed case in post-merge | 0 | - | 1 | 1次提交 |
| [#5529](https://github.com/NVIDIA/TensorRT-LLM/pull/5529) | feat(models): Mistral3.1 VLM pytorch backend support | 0 | - | 1 | 1次提交 |
| [#5491](https://github.com/NVIDIA/TensorRT-LLM/pull/5491) | Update trtllm-bench to support new Pytorch default. | 6 | • CI检查失败 (6次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/5491#issuecomment-) | 9 | 9次提交 |
| [#5460](https://github.com/NVIDIA/TensorRT-LLM/pull/5460) | chore: bump version to 1.0.0rc1 | 0 | - | 1 | 1次提交 |
| [#5428](https://github.com/NVIDIA/TensorRT-LLM/pull/5428) | feat: Make benchmark_serving part of the library | 3 | • CI检查失败 (3次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/5428#issuecomment-) | 1 | 1次提交 |
| [#5422](https://github.com/NVIDIA/TensorRT-LLM/pull/5422) | Fix none response in PD | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/5422#issuecomment-) | 1 | 1次提交 |
| [#5404](https://github.com/NVIDIA/TensorRT-LLM/pull/5404) | [#5403][perf] Conditionally enable SWAP AB for speculative decoding | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/5404#issuecomment-) | 4 | 4次提交 |
| [#5378](https://github.com/NVIDIA/TensorRT-LLM/pull/5378) | Fix: missing clientId when serialize and deserialize response (cherry-pick #5231 | 0 | - | 1 | 1次提交 |
| [#5363](https://github.com/NVIDIA/TensorRT-LLM/pull/5363) | [Infra]cherry pick sanity check yml change for 5080 and 5090 from main | 0 | - | 1 | 1次提交 |
| [#5360](https://github.com/NVIDIA/TensorRT-LLM/pull/5360) | [Infra]Fix l0_sanity_check.yml which also as gb202 and gb203 | 0 | - | 1 | 1次提交 |
| [#5337](https://github.com/NVIDIA/TensorRT-LLM/pull/5337) | Fix CI build time increase | 0 | - | 3 | 3次提交 |
| [#5334](https://github.com/NVIDIA/TensorRT-LLM/pull/5334) | doc: Include NGC release containers in quick-start-guide.md | 0 | - | 2 | 2次提交 |
| [#5333](https://github.com/NVIDIA/TensorRT-LLM/pull/5333) | [TRTLLM-3442] feat: added beam search support to the PyTorch Workflow | 2 | • Review Changes Requested (2次) - [Reviews](https://github.com/NVIDIA/TensorRT-LLM/pull/5333/files) | 18 | 18次提交 |
| [#5309](https://github.com/NVIDIA/TensorRT-LLM/pull/5309) | chore: bump version to 0.21.0rc3 | 0 | - | 1 | 1次提交 |
| [#5298](https://github.com/NVIDIA/TensorRT-LLM/pull/5298) | Revert "[infra] Report CI authorization errors to PR" | 0 | - | 1 | 1次提交 |
| [#5295](https://github.com/NVIDIA/TensorRT-LLM/pull/5295) | chore: Refine printed info of CHECK_TYPE. | 0 | - | 1 | 1次提交 |
| [#5258](https://github.com/NVIDIA/TensorRT-LLM/pull/5258) | [enhance] Add the ability to write a request timeline. | 0 | - | 4 | 4次提交 |
| [#5245](https://github.com/NVIDIA/TensorRT-LLM/pull/5245) | None - Some clean-ups for the automation pipeline | 0 | - | 3 | 3次提交 |
| [#5234](https://github.com/NVIDIA/TensorRT-LLM/pull/5234) | chore:[BREAKING CHANGE] use cacheTransceiverConfig as knobs for disagg service | 1 | • Review Changes Requested (1次) - [Reviews](https://github.com/NVIDIA/TensorRT-LLM/pull/5234/files) | 7 | 7次提交 |
| [#5230](https://github.com/NVIDIA/TensorRT-LLM/pull/5230) | chore: enable moe_backend on Qwen3 test | 0 | - | 5 | 5次提交 |
| [#5221](https://github.com/NVIDIA/TensorRT-LLM/pull/5221) | test: [CI] Add failed cases into waives.txt | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/5221#issuecomment-) | 1 | 1次提交 |
| [#5209](https://github.com/NVIDIA/TensorRT-LLM/pull/5209) | [fix] Fix Llama4 min-latency import error | 0 | - | 1 | 1次提交 |
| [#5200](https://github.com/NVIDIA/TensorRT-LLM/pull/5200) | fix: fix license bug | 0 | - | 2 | 2次提交 |
| [#5188](https://github.com/NVIDIA/TensorRT-LLM/pull/5188) | optimize memset before alltoall communication | 0 | - | 1 | 1次提交 |
| [#5183](https://github.com/NVIDIA/TensorRT-LLM/pull/5183) | feat: MoE trtllm backend kernel update | 0 | - | 1 | 1次提交 |
| [#5159](https://github.com/NVIDIA/TensorRT-LLM/pull/5159) | [TRTLLM-5758] test: Add Bielik-11B-v2.2 Model Support | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/5159#issuecomment-) | 1 | 1次提交 |
| [#5142](https://github.com/NVIDIA/TensorRT-LLM/pull/5142) | Add Wechat_Group_QR_Code.png to docs/source/media and main page of TR… | 0 | - | 2 | 2次提交 |
| [#5128](https://github.com/NVIDIA/TensorRT-LLM/pull/5128) | [TRTLLM-5835][feat] Optimized Mamba2Mixer prefill | 0 | - | 71 | 71次提交 |
| [#5125](https://github.com/NVIDIA/TensorRT-LLM/pull/5125) | [test] add nvfp4 DeepSeek-V3-Lite-mtp tests | 9 | • CI检查失败 (9次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/5125#issuecomment-) | 3 | 3次提交 |
| [#5122](https://github.com/NVIDIA/TensorRT-LLM/pull/5122) | feat: Support post_proc for bench | 0 | - | 6 | 6次提交 |
| [#5071](https://github.com/NVIDIA/TensorRT-LLM/pull/5071) | CI: waive test_ad_build_small_multi | 0 | - | 1 | 1次提交 |
| [#5054](https://github.com/NVIDIA/TensorRT-LLM/pull/5054) | [AutoDeploy] Merge Feature Branch Week 3 | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/5054#issuecomment-) | 3 | 3次提交 |
| [#5042](https://github.com/NVIDIA/TensorRT-LLM/pull/5042) | [fix] Unwaive test_llama_eagle3 | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/5042#issuecomment-) | 5 | 5次提交 |
| [#5020](https://github.com/NVIDIA/TensorRT-LLM/pull/5020) | fix #4974: A thread leak issue in scaffolding unittest | 0 | - | 1 | 1次提交 |
| [#4989](https://github.com/NVIDIA/TensorRT-LLM/pull/4989) | tests: fix some typo and limitation on test cases | 0 | - | 2 | 2次提交 |
| [#4973](https://github.com/NVIDIA/TensorRT-LLM/pull/4973) | fix:https://nvbugs/5324248 | 0 | - | 1 | 1次提交 |
| [#4969](https://github.com/NVIDIA/TensorRT-LLM/pull/4969) | Resubmit #4894 | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/4969#issuecomment-) | 18 | 18次提交 |
| [#4962](https://github.com/NVIDIA/TensorRT-LLM/pull/4962) | [TRTLLM-6088][doc] Add speculative decoding PyTorch docs | 0 | - | 1 | 1次提交 |
| [#4951](https://github.com/NVIDIA/TensorRT-LLM/pull/4951) | ci: [nvbugs/5280806] Unwaive unittests/_torch. | 5 | • CI检查失败 (5次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/4951#issuecomment-) | 2 | 2次提交 |
| [#4936](https://github.com/NVIDIA/TensorRT-LLM/pull/4936) | Raise shut down error for each request | 7 | • CI检查失败 (6次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/4936#issuecomment-)<br>• Review Changes Requested (1次) - [Reviews](https://github.com/NVIDIA/TensorRT-LLM/pull/4936/files) | 2 | 2次提交 |
| [#4921](https://github.com/NVIDIA/TensorRT-LLM/pull/4921) | fix: [nvbug 5321627] handle cases when TRT backend return more logits than outpu | 0 | - | 1 | 1次提交 |
| [#4920](https://github.com/NVIDIA/TensorRT-LLM/pull/4920) | Only pass `fast_build=true` to non-pytorch backend | 0 | - | 2 | 2次提交 |
| [#4906](https://github.com/NVIDIA/TensorRT-LLM/pull/4906) | feat: Add support for YARN in NemotronNAS models | 0 | - | 5 | 5次提交 |
| [#4897](https://github.com/NVIDIA/TensorRT-LLM/pull/4897) | fix: Fix broken vanilla moe since FusedMoE refactor. | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/4897#issuecomment-) | 1 | 1次提交 |
| [#4896](https://github.com/NVIDIA/TensorRT-LLM/pull/4896) | chore: bump version to 0.21.0rc1 | 0 | - | 1 | 1次提交 |
| [#4876](https://github.com/NVIDIA/TensorRT-LLM/pull/4876) | feat: Add support for fp8 rowwise quantization | 6 | • CI检查失败 (6次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/4876#issuecomment-) | 7 | 7次提交 |
| [#4864](https://github.com/NVIDIA/TensorRT-LLM/pull/4864) | fix: Register MoeLoadBalancerConfig to serialization.py | 0 | - | 2 | 2次提交 |
| [#4832](https://github.com/NVIDIA/TensorRT-LLM/pull/4832) | fix: [https://nvbugspro.nvidia.com/bug/5273945] Unwaive tests for bug-5273945 | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/4832#issuecomment-) | 1 | 1次提交 |
| [#4819](https://github.com/NVIDIA/TensorRT-LLM/pull/4819) | [TRTLLM-4987][feat] Support generation logits in TRTLLMSampler | 0 | - | 17 | 17次提交 |
| [#4818](https://github.com/NVIDIA/TensorRT-LLM/pull/4818) | feat: large-scale EP(part 6: Online EP load balancer integration for GB200 nvfp4 | 10 | • CI检查失败 (10次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/4818#issuecomment-) | 8 | 8次提交 |
| [#4804](https://github.com/NVIDIA/TensorRT-LLM/pull/4804) | [fix] Do not reuse dummy request KVCache | 1 | • Review Changes Requested (1次) - [Reviews](https://github.com/NVIDIA/TensorRT-LLM/pull/4804/files) | 1 | 1次提交 |
| [#4803](https://github.com/NVIDIA/TensorRT-LLM/pull/4803) | Expose new tech blog about DSR1 throughput optimization to the main R… | 0 | - | 1 | 1次提交 |
| [#4790](https://github.com/NVIDIA/TensorRT-LLM/pull/4790) | [Architecture] Refactor FusedMoE | 3 | • CI检查失败 (3次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/4790#issuecomment-) | 1 | 1次提交 |
| [#4766](https://github.com/NVIDIA/TensorRT-LLM/pull/4766) | fix: re-enable tp/pp for quickstart_advanced.py. | 0 | - | 2 | 2次提交 |
| [#4734](https://github.com/NVIDIA/TensorRT-LLM/pull/4734) | fix: iteration logging and typing in PyExecutor | 0 | - | 1 | 1次提交 |
| [#4713](https://github.com/NVIDIA/TensorRT-LLM/pull/4713) | fix: Mistral Small vision encoder with BS>1 | 0 | - | 1 | 1次提交 |
| [#4694](https://github.com/NVIDIA/TensorRT-LLM/pull/4694) | use cu for fmha_v2 | 0 | - | 10 | 10次提交 |
| [#4671](https://github.com/NVIDIA/TensorRT-LLM/pull/4671) | Update the description for NGC docker images | 0 | - | 1 | 1次提交 |
| [#4663](https://github.com/NVIDIA/TensorRT-LLM/pull/4663) | Add files into scan ignoreList | 0 | - | 1 | 1次提交 |
| [#4651](https://github.com/NVIDIA/TensorRT-LLM/pull/4651) | feat: chunked prefill for MLA (Blackwell) | 0 | - | 27 | 27次提交 |
| [#4623](https://github.com/NVIDIA/TensorRT-LLM/pull/4623) | [TRTLLM-1658][feat] Enable multiple response in trtllm-serve for TRT backend | 0 | - | 1 | 1次提交 |
| [#4613](https://github.com/NVIDIA/TensorRT-LLM/pull/4613) | fix: test trtllm-bench mgmn | 0 | - | 2 | 2次提交 |
| [#4611](https://github.com/NVIDIA/TensorRT-LLM/pull/4611) | feat: Integration of Fused QKNorm+RoPE. | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/4611#issuecomment-) | 9 | 9次提交 |
| [#4594](https://github.com/NVIDIA/TensorRT-LLM/pull/4594) | [TRTLLM-4647][fix] Fix the no fusion allreduce hanging | 4 | • CI检查失败 (4次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/4594#issuecomment-) | 5 | 5次提交 |
| [#4535](https://github.com/NVIDIA/TensorRT-LLM/pull/4535) | [TRTLLM-5070][feat] Support FP8 KV Cache Reuse for MLA | 0 | - | 3 | 3次提交 |
| [#4508](https://github.com/NVIDIA/TensorRT-LLM/pull/4508) | Chore: waive torch compile test cases of deepseek v3 lite | 0 | - | 1 | 1次提交 |
| [#4507](https://github.com/NVIDIA/TensorRT-LLM/pull/4507) | fix: Fix trtllm sampler beam width bug | 0 | - | 2 | 2次提交 |
| [#4489](https://github.com/NVIDIA/TensorRT-LLM/pull/4489) | fix: replace the image links in the blog | 0 | - | 1 | 1次提交 |
| [#4479](https://github.com/NVIDIA/TensorRT-LLM/pull/4479) | tests: update api change from decoder to sampler in test | 0 | - | 1 | 1次提交 |
| [#4434](https://github.com/NVIDIA/TensorRT-LLM/pull/4434) | [Docs] - Reapply #4220 | 0 | - | 2 | 2次提交 |
| [#4417](https://github.com/NVIDIA/TensorRT-LLM/pull/4417) | test: [CI] remove closed bugs | 0 | - | 2 | 2次提交 |
| [#4400](https://github.com/NVIDIA/TensorRT-LLM/pull/4400) | doc: [TRTLLM-325]Integrate the NGC image in Makefile automation and document | 0 | - | 5 | 5次提交 |
| [#4394](https://github.com/NVIDIA/TensorRT-LLM/pull/4394) | Feat: add chunked-attention kernels on Blackwell | 5 | • CI检查失败 (5次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/4394#issuecomment-) | 2 | 2次提交 |
| [#4393](https://github.com/NVIDIA/TensorRT-LLM/pull/4393) | Fix test_fused_moe_w4afp8 | 0 | - | 1 | 1次提交 |
| [#4386](https://github.com/NVIDIA/TensorRT-LLM/pull/4386) | doc： DS r1 min latency blog | 0 | - | 8 | 8次提交 |
| [#4376](https://github.com/NVIDIA/TensorRT-LLM/pull/4376) | Remove vila test | 0 | - | 1 | 1次提交 |
| [#4373](https://github.com/NVIDIA/TensorRT-LLM/pull/4373) | [AutoDeploy] fix: proper process group clean up | 0 | - | 1 | 1次提交 |
| [#4370](https://github.com/NVIDIA/TensorRT-LLM/pull/4370) | [AutoDeploy] eager pattern matcher new pattern | 0 | - | 1 | 1次提交 |
| [#4358](https://github.com/NVIDIA/TensorRT-LLM/pull/4358) | feat: Add pp support for hybrid attn/mamba model | 0 | - | 3 | 3次提交 |
| [#4348](https://github.com/NVIDIA/TensorRT-LLM/pull/4348) | Fix bias shape in weightOnlyGroupwiseQuantMatmulPlugin for TRT workflow | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/4348#issuecomment-) | 1 | 1次提交 |
| [#4300](https://github.com/NVIDIA/TensorRT-LLM/pull/4300) | [https://nvbugs/5277113][fix]genai-perf API change stress test | 0 | - | 2 | 2次提交 |
| [#4297](https://github.com/NVIDIA/TensorRT-LLM/pull/4297) | chore: reduce code duplication | 0 | - | 1 | 1次提交 |
| [#4263](https://github.com/NVIDIA/TensorRT-LLM/pull/4263) | Test: Improve model re-use in C++ DGX tests for CI stability | 0 | - | 11 | 11次提交 |
| [#4206](https://github.com/NVIDIA/TensorRT-LLM/pull/4206) | [CI] waive two multi-gpu test cases | 0 | - | 1 | 1次提交 |
| [#4191](https://github.com/NVIDIA/TensorRT-LLM/pull/4191) | infra: [TRTLLM-325] Prepare for NGC release - multiplatform build | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/4191#issuecomment-) | 4 | 4次提交 |
| [#4183](https://github.com/NVIDIA/TensorRT-LLM/pull/4183) | feat: Support Mistral Small 3.1 24B VLM in TRT workflow | 0 | - | 1 | 1次提交 |
| [#4176](https://github.com/NVIDIA/TensorRT-LLM/pull/4176) | test: amend default pytorch extra-llm-api-config.yml in perf test | 0 | - | 2 | 2次提交 |
| [#4161](https://github.com/NVIDIA/TensorRT-LLM/pull/4161) | [TRTLLM-5054][fix] Removing repeated loading of input processor | 0 | - | 2 | 2次提交 |
| [#4158](https://github.com/NVIDIA/TensorRT-LLM/pull/4158) | Add test case for kv memory estimation | 0 | - | 6 | 6次提交 |
| [#4155](https://github.com/NVIDIA/TensorRT-LLM/pull/4155) | Feat: support exporting softmax statistics and update the kernel-selection heuri | 0 | - | 2 | 2次提交 |
| [#4140](https://github.com/NVIDIA/TensorRT-LLM/pull/4140) | feat: Prefetch safetensors files before loading them | 0 | - | 2 | 2次提交 |
| [#4129](https://github.com/NVIDIA/TensorRT-LLM/pull/4129) | docs:add torch flow supported model list. | 0 | - | 1 | 1次提交 |
| [#4122](https://github.com/NVIDIA/TensorRT-LLM/pull/4122) | [Infra] - Update code ownership rules for public APIs | 0 | - | 2 | 2次提交 |
| [#4109](https://github.com/NVIDIA/TensorRT-LLM/pull/4109) | [Infra] - Update code ownership rules | 0 | - | 1 | 1次提交 |
| [#4098](https://github.com/NVIDIA/TensorRT-LLM/pull/4098) | doc: Update version switcher | 0 | - | 1 | 1次提交 |
| [#4095](https://github.com/NVIDIA/TensorRT-LLM/pull/4095) | [https://nvbugspro.nvidia.com/bug/5260676]test: skip fp8 quantization case for p | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/4095#issuecomment-) | 1 | 1次提交 |
| [#4074](https://github.com/NVIDIA/TensorRT-LLM/pull/4074) | [fix] Loosen the thresholds of test_attention_mla | 0 | - | 1 | 1次提交 |
| [#4065](https://github.com/NVIDIA/TensorRT-LLM/pull/4065) | [feat/] enable attention DP in Llama4 maverick model - part 1 | 0 | - | 8 | 8次提交 |
| [#4016](https://github.com/NVIDIA/TensorRT-LLM/pull/4016) | [Deepseek] Refactor Deepseek Decoder layer | 0 | - | 1 | 1次提交 |
| [#3972](https://github.com/NVIDIA/TensorRT-LLM/pull/3972) | fix[nvbug-5228840]: Remove test cases of feature not supported anymore | 3 | • CI检查失败 (3次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/3972#issuecomment-) | 10 | 10次提交 |
| [#3929](https://github.com/NVIDIA/TensorRT-LLM/pull/3929) | [NVBUG 5247699]Fix mixtral fp4 llmapi bug. | 0 | - | 1 | 1次提交 |
| [#3926](https://github.com/NVIDIA/TensorRT-LLM/pull/3926) | Cherry pick https://github.com/NVIDIA/TensorRT-LLM/pull/3906/ | 0 | - | 1 | 1次提交 |
| [#3925](https://github.com/NVIDIA/TensorRT-LLM/pull/3925) | unwaive disagg tests | 0 | - | 1 | 1次提交 |
| [#3899](https://github.com/NVIDIA/TensorRT-LLM/pull/3899) | feat: fix erros on scaffolding README | 0 | - | 1 | 1次提交 |
| [#3885](https://github.com/NVIDIA/TensorRT-LLM/pull/3885) | feat: support multi lora adapters and TP | 0 | - | 9 | 9次提交 |
| [#3863](https://github.com/NVIDIA/TensorRT-LLM/pull/3863) | fix: Fix FMHA-based MLA in the generation phase and add MLA unit test | 0 | - | 7 | 7次提交 |
| [#3859](https://github.com/NVIDIA/TensorRT-LLM/pull/3859) | infra: [TRTLLM-4475][TRTLLM-4565] Add pipeline hierarchy and basic info in the J | 0 | - | 6 | 6次提交 |
| [#3855](https://github.com/NVIDIA/TensorRT-LLM/pull/3855) | feat: Add multimodal embedding field in LlmRequest | 0 | - | 10 | 10次提交 |
| [#3841](https://github.com/NVIDIA/TensorRT-LLM/pull/3841) | chore: Mass integration of release/0.19 into main | 6 | • CI检查失败 (6次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/3841#issuecomment-) | 1 | 1次提交 |
| [#3832](https://github.com/NVIDIA/TensorRT-LLM/pull/3832) | Fix: Revert commit 25f9669 | 0 | - | 1 | 1次提交 |
| [#3787](https://github.com/NVIDIA/TensorRT-LLM/pull/3787) | fix: remove the unnecessary metadata changes in mtp | 0 | - | 1 | 1次提交 |
| [#3765](https://github.com/NVIDIA/TensorRT-LLM/pull/3765) | Add log_level for disaggregated_mpi_worker | 0 | - | 1 | 1次提交 |
| [#3761](https://github.com/NVIDIA/TensorRT-LLM/pull/3761) | Fix: nvbugs/5234210 ModelOpt Mixtral AWQ OOM (cherry-picking to release/0.19) | 0 | - | 1 | 1次提交 |
| [#3760](https://github.com/NVIDIA/TensorRT-LLM/pull/3760) | chore: add pull request template | 0 | - | 3 | 3次提交 |
| [#3691](https://github.com/NVIDIA/TensorRT-LLM/pull/3691) | Report number of context tokens in one iteration | 2 | • CI检查失败 (2次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/3691#issuecomment-) | 6 | 6次提交 |
| [#3687](https://github.com/NVIDIA/TensorRT-LLM/pull/3687) | chore: Waive disaggregated load balance | 0 | - | 1 | 1次提交 |
| [#3642](https://github.com/NVIDIA/TensorRT-LLM/pull/3642) | fix: Pick waives from main | 0 | - | 1 | 1次提交 |
| [#3585](https://github.com/NVIDIA/TensorRT-LLM/pull/3585) | fix: nvbugs/5075538: fix cross attention mask when decoder input len > 1 | 0 | - | 2 | 2次提交 |
| [#3584](https://github.com/NVIDIA/TensorRT-LLM/pull/3584) | feat: Disaggregated router class | 0 | - | 8 | 8次提交 |
| [#3563](https://github.com/NVIDIA/TensorRT-LLM/pull/3563) | fix: amend trtllm-bench command in the test | 0 | - | 1 | 1次提交 |
| [#3553](https://github.com/NVIDIA/TensorRT-LLM/pull/3553) | Clean up linear.py, mlp.py, gated_mlp.py | 0 | - | 1 | 1次提交 |
| [#3550](https://github.com/NVIDIA/TensorRT-LLM/pull/3550) | fix: remove extraneous local docker user command | 0 | - | 1 | 1次提交 |
| [#3510](https://github.com/NVIDIA/TensorRT-LLM/pull/3510) | test: [CI] remove closed bugs | 0 | - | 1 | 1次提交 |
| [#3506](https://github.com/NVIDIA/TensorRT-LLM/pull/3506) | refactor: Introduce DecoderOutputBuffers per batch | 0 | - | 6 | 6次提交 |
| [#3497](https://github.com/NVIDIA/TensorRT-LLM/pull/3497) | fix: add kv memory size per token of draft model to calculate max number of toke | 1 | • CI检查失败 (1次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/3497#issuecomment-) | 2 | 2次提交 |
| [#3435](https://github.com/NVIDIA/TensorRT-LLM/pull/3435) | fix: Fix the issues related to fused moe path. | 0 | - | 2 | 2次提交 |
| [#3384](https://github.com/NVIDIA/TensorRT-LLM/pull/3384) | fix: Use hmac authentication for pickle encryption | 4 | • CI检查失败 (4次) - [PR Comments](https://github.com/NVIDIA/TensorRT-LLM/pull/3384#issuecomment-) | 4 | 4次提交 |
| [#2830](https://github.com/NVIDIA/TensorRT-LLM/pull/2830) | Use NVIDIA-gha runners to collect test results for CI | 0 | - | 1 | 1次提交 |

---

## 统计摘要

- **总PR数**: 441
- **直接合入PR**: 257 (58.3%)
- **被阻塞PR**: 184 (41.7%)

### 阻塞次数分布

| 阻塞次数 | PR数量 | 占比 |
|---|---|---|
| 0次（直接合入） | 257 | 58.3% |
| 1次 | 53 | 12.0% |
| 2次 | 39 | 8.8% |
| 3-5次 | 57 | 12.9% |
| 6-10次 | 35 | 7.9% |

### Commit次数分布

| Commit次数 | PR数量 | 占比 |
|---|---|---|
| 1次 | 210 | 47.6% |
| 2-3次 | 115 | 26.1% |
| 4-5次 | 41 | 9.3% |
| 6-10次 | 46 | 10.4% |
| 10+次 | 29 | 6.6% |

---

## 对比：改进前 vs 改进后

| 指标 | 改进前 | 改进后 | 变化 |
|------|--------|--------|------|
| 直接合入率 | 21.8% | 待统计 | 预计提升 |
| 被阻塞率 | 78.2% | 待统计 | 预计下降 |
| 检测方法 | 宽松（误判多） | 严格（准确） | - |

**说明**: 改进后排除了大量误判，如：
- CodeRabbitAI的静态检查警告
- Bot命令中的"failed"关键词
- 讨论中提到的"fix failed test"

---

**报告生成时间**: 2026-01-27 (改进版)

**数据来源**: GitHub API (NVIDIA/TensorRT-LLM)

**改进说明**: 使用更严格的CI失败检测逻辑，排除了大量误判情况