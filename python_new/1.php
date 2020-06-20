<?php
$sql = "SELECT * FROM `article` WHERE ";
if($cat_id){
    $where = "cat = " . $cat_id;
} else {
    $where = "1 = 1";
}
$sql .= $where;
