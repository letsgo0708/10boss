<script>
    import { link } from 'svelte-spa-router'
    import { push } from 'svelte-spa-router'
    import fastapi from "../lib/api"
    import Error from "../components/Error.svelte"
    import moment from 'moment/min/moment-with-locales'
    moment.locale('ko')

    export let params = {}
    let cut_id = params.cut_id

    let cut = ""
    let boss_id = 0
    let cut_time = ""
    let create_time = ""
    let error = { detail:[] }

    let today = new Date();
    let h = today.getHours().toString();
    let m = today.getMinutes().toString();

    function get_cut() {
        fastapi("get", "/api/cut/detail/" + cut_id, {}, (json) => {
        console.log(json)
        cut = json
        boss_id = cut.boss_id
        cut_time = cut.cut_time
        create_time = cut.create_time
    })
}

get_cut()

    function delete_cut(cut_id) {
        let url = "/api/cut/delete"
        let params = {cut_id: cut_id};
        fastapi("delete", url, params, 
            (json) => {
                get_cut()
        })
    }
</script>


{cut_time}
{create_time}



<div>
    <button on:click={ () => delete_cut(cut_id)}>
    삭제하기
    </button>
</div>
 
<div>
    <button on:click="{() => {
        push('/')
        }}">목록으로
    </button>
</div>