<script>
    export let error // 전 달 받 은 오 류
</script>

{#if typeof error.detail === 'string'}
    <div class="alert alert-danger" role="alert">
        <div>
            {error.detail}
        </div>
    </div>
{:else if typeof error.detail === 'object' && error.detail.length > 0 }
    <div class="alert alert-danger" role="alert">
        {#each error.detail as err, i}
        <div>
            {err.msg}
        </div>
        {/each}
    </div>
{/if}