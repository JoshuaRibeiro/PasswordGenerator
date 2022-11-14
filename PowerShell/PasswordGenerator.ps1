$csv = Import-CSV -Path ($PSScriptRoot + '\CSV\dictionary.csv')
$dictionary = [System.Collections.ArrayList]::new()

ForEach ($word in $csv) {
    if ($word.a.length -gt 3 -and $word.a.length -lt 6 -and -not $dictionary.contains($word.a)) {
        $dictionary += $word.a
    }
}

$symbols = '!', '@', '$', '%', '^', '&', '*', '-', '_', '+', '=', ':', '|', '~', '?', '/', '.', ';'

$length = $args[0]
$pwd = ''

Do {
    $pwd = $pwd + (Get-Culture).TextInfo.ToTitleCase((Get-Random -InputObject $dictionary))

    if ($pwd.Length -gt $length-3) {
        $pwd = ''
    }
    elseif ($pwd.Length -gt $length-5) {
        $diff = $length-$pwd.length
        $pwd = $pwd + ('!' * ($diff))
    }

} While ($pwd.Length -lt $length)

$pwd = $pwd.Remove($pwd.Length-$diff)

$pwd = $pwd + (( (1..($diff-1)) | ForEach-Object {Get-Random -Minimum 0 -Maximum 9} ) -join '')

Return $pwd + ($symbols | Get-Random)