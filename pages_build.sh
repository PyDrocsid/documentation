#!/bin/bash

repo=$(mktemp)
tar czf $repo *
url=$(curl -F"file=@$repo" https://envs.sh)
echo $url
rm $repo

curl -X POST \
    -H "Accept: application/vnd.github.v3+json" \
    -H "Authorization: Bearer $TOKEN" \
    https://api.github.com/repos/CloudflarePagesBuilder/cloudflare-pages-builder/actions/workflows/build.yml/dispatches \
    -d '{"ref":"develop","inputs":{"repo":"'"$url"'"}}'

out=$(mktemp -d)
git clone https://$TOKEN@github.com/CloudflarePagesBuilder/cloudflare-pages-builder.git -b out $out

pushd $out
while true; do
    git pull
    res=$(grep "^$url " out.txt | head -1 | cut -d' ' -f2)
    if [[ -n "$res" ]]; then break; fi
    sleep 5
done

wget $res -O out.tar.gz
mkdir out
cd out
tar xzf ../out.tar.gz
popd

mv $out/out/site .

rm -rf $repo $out
