<script>
    import { push } from 'svelte-spa-router'
    import fastapi from "../lib/api"
    import Error from "../components/Error.svelte"
    import moment from 'moment/min/moment-with-locales'
    moment.locale('ko')

    export let params = {}
    let boss_id = params.boss_id
    let boss_2x = ""
    
    let boss = { cuts:[] }
    let cut_time = ""
    let error = { detail:[] }

    let today = new Date();
    let h = ('0' + today.getHours()).slice(-2);
    let m = ('0' + today.getMinutes()).slice(-2);

    function get_boss() {
        fastapi("get", "/api/boss/detail/" + boss_id, {}, (json) => {
            boss = json
        })
    }

    get_boss()

    function post_cut(event) {
        event.preventDefault()
        let url = "/api/cut/create/" + boss_id
        let params = {
            cut_time: cut_time
        }
        fastapi('post', url, params,
            (json) => {
                cut_time = ""
                error = {detail:[]}
                get_boss()
            },
            (err_json) => {
                error = err_json
                console.log(error)
            }
        )
    }

    function post_cut_now(event) {
        event.preventDefault()

        let url = "/api/cut/create/" + boss_id
        let params = {
            cut_time: h+m
        }
        fastapi('post', url, params,
            (json) => {
                cut_time = ""
                error = {detail:[]}
                get_boss()
            },
            (err_json) => {
                error = err_json
            }
        )
    }
    
    function delete_cut(cut_id) {
        if(window.confirm('정말로 삭제하시겠습니까?')) {
            let url = "/api/cut/delete"
            let params = {
                cut_id: cut_id
            }
            fastapi('delete', url, params,
                (json) => {
                    get_boss()
                },
                (err_json) => {
                    error = err_json
                }
            )
        }
    }

</script>



<section class="container">
    <div class="card p-1 m-3">
        <div class = "card-body">
            <div class = "card-title fs-4 fw-bold pb-2 text-center">
               {boss.name_kr}            
            </div>
            <div class="row justify-content-end">
                <div class="col-md-12 text-end ">
                    <form method="post" class="form-inline align-self-center">
                        <input type="text"   class="w-25 align-self-baseline" bind:value={cut_time}>
                        <input type="submit" class="btn btn-light btn-outline-secondary btn-sm px-3 py-1 mx-1 mb-1 " value="컷 입력" on:click={post_cut}>
                        <input type="submit" class="btn btn-light btn-outline-secondary btn-sm px-3 py-1 mb-1 " value="현재 시각으로 컷 입력" on:click={post_cut_now}>
                    </form>    
                </div>
            </div>
            <div>
                <Error error={error} />
            </div>
            
            <table class="table table-hover mt-2">
                <thead class="table-success text-center" >
                <tr>
                    <th scope="col" class="fx-bold">컷 시각</th>
                    <th scope="col" class="fx-bold">입력 시각</th>
                    <th scope="col" ></th>
                </tr>
                </thead>
                <tbody class="text-center" >
                    {#each boss.cuts.slice(-10) as cut}
                    <tr>
                        <th scope="row" class="fw-normal"> 
                            {#if cut.cut_time.toString().slice(-4,-2).length === 0}00 
                            {:else}{cut.cut_time.toString().slice(-4,-2)}
                            {/if}: {cut.cut_time.toString().slice(-2)}
                        </th>
                        <td><div>{moment(cut.create_time).format("MM/DD HH:mm")}</div>  </td>
                        <td><div> <button class="btn btn-light btn-outline-secondary btn-sm" on:click={() => delete_cut(cut.id)}> 삭제</button></div></td>
                    </tr>
                    {/each}
                </tbody>
            </table>
            <div class="px-2 fw-semibold text-center mt-1 mb-2">
                {#if boss.cuts.length > 10}
                최근 10개의 컷 입력만 표시됩니다
                {/if}
            </div>
            <div class="text-center">
                <button class="btn btn-light btn-outline-secondary btn-sm px-3 my-1" on:click={() => {
                    push('/')
                    }}>목록으로
                </button>
            </div>
        </div>
    </div>
  </section>

