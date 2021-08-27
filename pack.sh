#!/bin/bash
utils_files="mysql_data.py,hive_data.py,cipher.py,es_twins.py,es_index.py,es_search.py"
project_files="utils,config.py,*search.py,server*.py,start*.sh,stop*.sh"

copy_files(){
    src=$1
    dest=$2
    files=(${3//,/ })
    for file in ${files[@]}
    do
        cp -r ${src}/${file} ${dest}/
    done
}

project_path=$(cd $(dirname $0); pwd)
project_name="${project_path##*/}"
utils_path=$(dirname ${project_path})/utils

cd ${project_path}
rm -rf ${project_name}.tar.gz
mkdir -p ${project_name}/utils ${project_name}/logs
copy_files ${utils_path} ${project_name}/utils ${utils_files}
copy_files . ${project_name} ${project_files}
tar -czf ${project_name}.tar.gz ${project_name}
rm -rf ${project_name}